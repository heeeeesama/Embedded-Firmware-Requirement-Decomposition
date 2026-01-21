import re
import sys
import json
import csv
import os
import glob


def parse_markdown_file(file_path):
    """解析单个Markdown文件"""
    heading_tree = []
    root_node = {'level': 0, 'children': heading_tree, 'path': []}
    stack = [root_node]
    text_blocks = []  # 存储所有文本块

    # 支持ATX标题格式
    atx_pattern = re.compile(r'^(#{1,6})\s+(.+?)\s*#*\s*$')

    # 表格检测模式
    table_pattern = re.compile(r'^\s*\|')

    # 元数据标记检测
    metadata_pattern = re.compile(r'^---$')
    in_metadata = False
    found_first_heading = False

    with open(file_path, 'r', encoding='utf-8') as f:
        buffer = []  # 当前章节的内容缓冲区

        for line in f:
            line = line.rstrip()

            # 检查元数据块
            if metadata_pattern.match(line):
                in_metadata = not in_metadata
                continue

            # 跳过元数据行
            if in_metadata:
                continue

            # 处理ATX标题
            atx_match = atx_pattern.match(line)
            if atx_match:
                found_first_heading = True
                level = len(atx_match.group(1))
                text = atx_match.group(2).strip()

                # 遇到新标题时，将缓冲区内容保存为一个块（如果非空）
                if buffer and any(len(l.strip()) > 0 for l in buffer):
                    # 检查缓冲区中是否有实际内容
                    text_blocks.append({
                        'path': ">".join(stack[-1]['path']) if stack else "",
                        'text': "\n".join(buffer),
                        'token_count': count_tokens(buffer),  # 添加token计数
                        'source_file': os.path.basename(file_path)  # 添加源文件名
                    })
                    buffer = []

                # 更新章节树 - 找到正确父节点
                # 弹出所有大于或等于当前level的节点
                while len(stack) > 1 and stack[-1]['level'] >= level:
                    stack.pop()

                # 新节点的路径 = 父节点路径 + 当前标题
                parent_path = stack[-1]['path'].copy()
                new_path = parent_path + [text]

                # 创建新节点
                new_node = {
                    'text': text,
                    'level': level,
                    'children': [],
                    'path': new_path  # 存储完整路径
                }

                # 添加到父节点的children
                stack[-1]['children'].append(new_node)

                # 将新节点推入堆栈
                stack.append(new_node)
                continue

            # 处理表格内容
            if table_pattern.match(line):
                # 只有在已经开始内容时才添加表格
                if found_first_heading:
                    buffer.append(line)
                continue

            # 处理普通内容 - 仅在找到第一个标题后
            if found_first_heading and line.strip():
                buffer.append(line)

    # 处理文件末尾的剩余内容
    if buffer and any(len(l.strip()) > 0 for l in buffer):
        text_blocks.append({
            'path': ">".join(stack[-1]['path']) if stack else "",
            'text': "\n".join(buffer),
            'token_count': count_tokens(buffer),  # 添加token计数
            'source_file': os.path.basename(file_path)  # 添加源文件名
        })

    return text_blocks


def count_tokens(content_lines):
    """计算内容块中的token数量（简单分词）"""
    token_count = 0
    for line in content_lines:
        # 简单分词：以空格分割
        tokens = line.split()
        token_count += len(tokens)
    return token_count


def process_folder(folder_path):
    """处理文件夹中的所有Markdown文件"""
    all_text_blocks = []

    # 查找所有Markdown文件
    md_files = glob.glob(os.path.join(folder_path, '**/*.md'), recursive=True)
    md_files += glob.glob(os.path.join(folder_path, '**/*.markdown'), recursive=True)

    if not md_files:
        print(f"No Markdown files found in {folder_path}")
        return []

    print(f"Found {len(md_files)} Markdown files to process")

    # 处理每个文件
    for i, file_path in enumerate(md_files, 1):
        print(f"Processing file {i}/{len(md_files)}: {os.path.basename(file_path)}")
        try:
            text_blocks = parse_markdown_file(file_path)
            all_text_blocks.extend(text_blocks)
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")

    return all_text_blocks


def export_to_tsv(text_blocks, output_file):
    """导出文本块到TSV文件（三列：id, text, title）"""
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter='\t')
        # 写入标题行
        writer.writerow(['id', 'text', 'title'])

        # 为每个块分配ID（从1开始）
        for i, block in enumerate(text_blocks, 1):
            title = block['path'] if block['path'] else ''
            text = block['text'].replace('\n', ' ')  # 替换换行符

            # 添加源文件名到标题（可选）
            # title = f"[{block['source_file']}] {title}"

            # 仅导出有实际内容的块
            if text.strip():
                writer.writerow([i, text, title])

    print(f"Exported to TSV: {output_file}")


def print_summary(text_blocks):
    """打印内容块统计摘要"""
    total_blocks = len(text_blocks)
    total_tokens = sum(block.get('token_count', 0) for block in text_blocks)

    if total_blocks == 0:
        print("No content blocks found")
        return

    # 找出token数量最多的块
    longest_block = max(text_blocks, key=lambda x: x.get('token_count', 0))
    # 找出token数量最少的块
    shortest_block = min(text_blocks, key=lambda x: x.get('token_count', 0))
    # 计算平均token数量
    avg_tokens = total_tokens / total_blocks

    print("\nContent Block Summary:")
    print(f"Total blocks: {total_blocks}")
    print(f"Total tokens: {total_tokens}")
    print(f"Average tokens per block: {avg_tokens:.1f}")
    print(f"Longest block ({longest_block['token_count']} tokens):")
    print(f"  Title: {longest_block['path']}")
    print(f"  Source: {longest_block['source_file']}")
    print(f"  Preview: {longest_block['text'][:50]}...")
    print(f"Shortest block ({shortest_block['token_count']} tokens):")
    print(f"  Title: {shortest_block['path']}")
    print(f"  Source: {shortest_block['source_file']}")
    print(f"  Preview: {shortest_block['text'][:50]}...")

    # 按文件统计
    file_stats = {}
    for block in text_blocks:
        file_name = block['source_file']
        file_stats.setdefault(file_name, {'blocks': 0, 'tokens': 0})
        file_stats[file_name]['blocks'] += 1
        file_stats[file_name]['tokens'] += block.get('token_count', 0)

    print("\nFile Statistics:")
    for file_name, stats in file_stats.items():
        print(f"  {file_name}: {stats['blocks']} blocks, {stats['tokens']} tokens")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    try:
        # 处理文件夹中的所有Markdown文件
        all_text_blocks = process_folder(folder_path)

        if not all_text_blocks:
            print("No content blocks found in any files")
            sys.exit(0)

        # 导出到TSV（三列格式）
        tsv_file = os.path.join(folder_path, 'bmc_chunks.tsv')
        export_to_tsv(all_text_blocks, tsv_file)

        # 打印内容块统计摘要
        print_summary(all_text_blocks)

        # 打印处理完成消息
        print(f"\nProcessed {len(all_text_blocks)} content blocks from all files")
        print(f"TSV file saved to: {tsv_file}")

    except Exception as e:
        print(f"Error processing folder: {str(e)}")
        import traceback

        traceback.print_exc()