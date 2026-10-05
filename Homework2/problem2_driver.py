import sys
from problem2 import SinglyLinkedList


def parse_value(val_str):
    """尝试将输入的字符串转为整数，若不行则保留原字符串"""
    try:
        return int(val_str)
    except ValueError:
        return val_str


def main():
    sll = SinglyLinkedList()

    for line in sys.stdin:
        line = line.strip()

        # 忽略空行和以 # 开头的注释行
        if not line or line.startswith('#'):
            continue

        parts = line.split()
        cmd = parts[0]
        args = parts[1:]

        try:
            if cmd == "append":
                if len(args) != 1:
                    print(f"Warning: 'append' expects 1 argument, got {len(args)}")
                    continue
                sll.append(parse_value(args[0]))

            elif cmd == "prepend":
                if len(args) != 1:
                    print(f"Warning: 'prepend' expects 1 argument, got {len(args)}")
                    continue
                sll.prepend(parse_value(args[0]))

            elif cmd == "insert":
                if len(args) != 2 or not args[0].isdigit():
                    print("Warning: Invalid arguments for 'insert'")
                    continue
                sll.insert(int(args[0]), parse_value(args[1]))

            elif cmd == "get":
                if len(args) != 1 or not args[0].isdigit():
                    print("Warning: Invalid argument for 'get'")
                    continue
                val = sll.get(int(args[0]))
                print(val)

            elif cmd == "find":
                if len(args) != 1:
                    print("Warning: 'find' expects 1 argument")
                    continue
                pos = sll.find(parse_value(args[0]))
                print(pos)

            elif cmd == "len":
                if len(args) != 0:
                    print("Warning: 'len' expects 0 arguments")
                    continue
                print(len(sll))

            elif cmd == "update":
                if len(args) != 2 or not args[0].isdigit():
                    print("Warning: Invalid arguments for 'update'")
                    continue
                sll.update(int(args[0]), parse_value(args[1]))

            elif cmd == "delete":
                if len(args) != 1:
                    print("Warning: 'delete' expects 1 argument")
                    continue
                success = sll.delete(parse_value(args[0]))
                if not success:
                    print(f"Warning: Value '{args[0]}' not in list")

            elif cmd == "delete_at":
                if len(args) != 1 or not args[0].isdigit():
                    print("Warning: Invalid argument for 'delete_at'")
                    continue
                val = sll.delete_at(int(args[0]))
                print(val)

            elif cmd == "print_list":
                if len(args) != 0:
                    print("Warning: 'print_list' expects 0 arguments")
                    continue
                sll.print_list()

            else:
                print(f"Warning: Unknown command '{cmd}'")

        except IndexError as e:
            print(f"Warning: Index error occurred ({e})")
        except Exception as e:
            print(f"Warning: Error executing '{cmd}' ({e})")

    # 处理完所有指令后，打印最终链表状态
    sll.print_list()


if __name__ == "__main__":
    main()