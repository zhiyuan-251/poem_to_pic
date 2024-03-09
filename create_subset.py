from fontTools.subset import main as subset_main

def create_subset_font(input_string, original_font_path, output_font_path):
    # 原始字体文件路径，输出子集字体文件路径
    # 指定需要保留的字符
    text_to_keep = input_string

    # 执行字体子集化命令
    cmd_args = [
        original_font_path,
        f"--text={text_to_keep}",
        f"--output-file={output_font_path}"
    ]
    subset_main(cmd_args)

    print(f"已生成子集字体文件：{output_font_path}")
