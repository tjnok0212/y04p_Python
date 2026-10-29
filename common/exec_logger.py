# -*- coding: utf-8 -*-

import inspect

def run_and_done(code_str, scope_dict=None):
    # 呼び出し元のフレーム（一つ前の呼び出し元）を取得
    frame = inspect.currentframe().f_back
    
    if scope_dict is None:
        # スコープが指定されていない場合は呼び出し元の環境を自動取得
        global_vars = frame.f_globals
        local_vars = frame.f_locals
    else:
        # 指定されている場合はその辞書を使用
        global_vars = scope_dict
        local_vars = scope_dict
    
    # 1. 希望のフォーマットで出力
    print("-"*30 + f"\n>>> {code_str}")

    # 2. 取得したスコープでコードを実行
    exec(code_str, global_vars, local_vars)



def show_env(env, filtered=True):
    if filtered:
        # __builtins__ を除外した辞書を作る
        display_env = {k: v for k, v in env.items() if k != '__builtins__'}
    else:
        # そのままの辞書を使う
        display_env = env
        
    print(display_env)
    return display_env  # 必要であれば辞書データを返すようにすると便利です


if __name__ == "__main__":
    # --- 使い方 ---
    # 変数を管理するための辞書を用意する
    env = {"x": 10}

    # 辞書を介して実行・書き換えを行う
    run_and_done("x = x + 20", env)
    run_and_done("y = x * 2", env)

    # print(env)  # 出力: {'x': 30, 'y': 60}

    # # __builtins__ を除いた変数だけを表示する例
    # filtered_env = {k: v for k, v in env.items() if k != '__builtins__'}
    # print(filtered_env)  # 出力: {'x': 30, 'y': 60}

    show_env(env)