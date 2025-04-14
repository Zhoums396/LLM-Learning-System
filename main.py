def say_hello():
    name = input("请输入您的名字: ")
    print(f"你好, {name}! 很高兴见到你!")
    print("请输入您的年龄: ")
    age = input()
    print(f"您今年{age}岁")

if __name__ == "__main__":
    say_hello()
    
    # 询问用户的爱好
    hobby = input("您有什么爱好吗? ")
    print(f"原来您喜欢{hobby}啊,这很有趣!")
    
    # 询问用户的职业
    job = input("您是做什么工作的? ")
    print(f"{job}是一个很棒的职业!")
    
    # 结束对话
    print("很高兴认识您,祝您今天愉快!")
