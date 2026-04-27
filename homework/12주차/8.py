with open("./pizza_file1.txt", "w", encoding="utf-8") as file:
    file.write("페퍼로니피자 3000\n")
    file.write("치즈피자 3200\n")
    file.write("콤비네이션피자 3500\n")
    
with open("./pizza_file1.txt", "a", encoding="utf-8") as file:
    file.write("불고기피자 3600\n")
    file.write("해산물피자 3800\n")