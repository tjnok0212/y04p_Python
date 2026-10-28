import sys

# 各行が実行されるときに呼ばれるトレース関数
def trace_lines(frame, event, arg):
    if event == 'line':
        lineno = frame.f_lineno
        filename = frame.f_code.co_filename
        
        # 自分自身のファイル内のコード行のみを表示対象にする
        if filename == __file__:
            with open(filename, 'r', encoding='utf-8') as f:
                code_line = f.readlines()[lineno - 1].strip()
            # 実行内容を表示
            print(f"-> {code_line}")
    return trace_lines


if __name__ == "__main__":
    # トレースを有効化
    sys.settrace(trace_lines)

    # --- 実行したい通常のコード ---
    x = 10 + 20
    y = x * 2
    print(f"Done: y = {y}")