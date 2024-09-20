import json
import readline
import sys

from .sdk import llm_chat, task_publish


def setup_readline():
    """配置 readline 以支持命令历史记录和自动补全"""
    history_path = ".bash_history"  # 存储历史记录的文件
    try:
        readline.read_history_file(history_path)
    except FileNotFoundError:
        pass  # 如果文件不存在，忽略错误
    sys.exitfunc = lambda: readline.write_history_file(history_path)


def greet():
    print("Hello! Welcome to the watcher interpreter.")
    print("------")


def check_config(user, pwd, eui):
    if not user or not pwd or not eui:
        print("Configuration is not complete. Please set user, pwd, and eui.")
        print("  setUser <username> - set username of APIkey")
        print("  setPwd <password> - set password of APIkey")
        print("  setEui <eui> - set eui of Watcher")
        print("------")
        return False
    return True


def show_help():
    print("Available commands:")
    print("  checkInfo - show all configs value")
    print("  setUser <username> - set username of APIkey")
    print("  setPwd <password> - set password of APIkey")
    print("  setEui <eui> - set eui of Watcher")
    print("  setBaseUrl <url> - set url of openAPI")
    print("  exit - Exits the program")
    print("--- After user,pwd,eui setted ---")
    print("  llm_chat <words> - Send a chat message to an API")
    print("  chat_publish <words> - chat for a task, and publish to watcher")
    print("  chat <words> - chat with watcher ")
    print("  task_publish <task> - Send a task to an API")
    print("------")


def run_script():
    setup_readline()
    greet()
    try:
        base_url = "https://sensecap.seeed.cc/openapi/"
        user = ""  # 初始为空，需要用户配置
        pwd = ""  # 初始为空，需要用户配置
        eui = ""  # 初始为空，需要用户配置

        while True:
            command = input("> ").strip().split()
            if not command:
                continue
            if command[0] == "exit":
                print("Exiting...")
                break
            elif command[0] == "checkInfo" and len(command) == 1:
                if check_config(user, pwd, eui):
                    print(f"The User is {user}")
                    print(f"The Password is {pwd}")
                    print(f"The EUI is {eui}")
                    print("All configs OK, try command. such as:")
                    print("  chat <words> - chat with watcher ")
                    print("------")
            elif command[0] == "setUser" and len(command) == 2:
                user = command[1]
                print("set User ok.")
                print("------")
            elif command[0] == "setPwd" and len(command) == 2:
                pwd = command[1]
                print("set Pwd ok.")
                print("------")
            elif command[0] == "setEui" and len(command) == 2:
                eui = command[1]
                print("set Eui ok.")
                print("------")
            elif command[0] == "setBaseUrl" and len(command) == 2:
                base_url = command[1]
                print("set BaseUrl ok.")
                print("------")
            elif command[0] == "llm_chat" and len(command) > 1:
                if check_config(user, pwd, eui):
                    try:
                        words = " ".join(command[1:])
                        result = llm_chat(words, base_url, user, pwd, eui)
                        print("Watcher: ", result)
                    except Exception as e:
                        print(e)
                    print("------")
            elif command[0] == "llm_task" and len(command) > 1:
                if check_config(user, pwd, eui):
                    try:
                        words = " ".join(command[1:])
                        result = llm_chat(words, base_url, user, pwd, eui)
                        print("Task:", json.dumps(result.get("data")))
                    except Exception as e:
                        print(e)
                    print("------")
            elif command[0] == "task_publish" and len(command) > 1:
                if check_config(user, pwd, eui):
                    try:
                        words = " ".join(command[1:])
                        task = json.loads(words)
                        result = task_publish(task, base_url, user, pwd, eui)
                        print("Watcher:", result)
                    except Exception as e:
                        print(e)
                    print("------")

            elif command[0] == "chat_publish" and len(command) > 1:
                if check_config(user, pwd, eui):
                    try:
                        words = " ".join(command[1:])
                        task = llm_chat(words, base_url, user, pwd, eui)
                        # print(task.get("data"))
                        result = task_publish(
                            task.get("data"), base_url, user, pwd, eui
                        )
                        print("Watcher:", result)
                    except Exception as e:
                        print(e)
                    print("------")

            elif command[0] == "chat" and len(command) > 1:
                if check_config(user, pwd, eui):
                    try:
                        words = " ".join(command[1:])
                        task = llm_chat(words, base_url, user, pwd, eui)
                        print(
                            f'Watcher: {task.get("data").get("task_flow")[0].get("params").get("response")}'
                        )
                    except Exception as e:
                        print(e)
                    print("------")
            else:
                print(
                    "Invalid command or arguments. Type 'help' for a list of commands."
                )
                show_help()
    except KeyboardInterrupt:
        print("\nExiting due to KeyboardInterrupt (Ctrl+C)...")
        sys.exit(0)


if __name__ == "__main__":
    run_script()
