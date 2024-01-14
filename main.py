import module.write as write
from module.date import date
import module.git as git
import module.img as img

if __name__=="__main__":
    print("请吧图片命名为img.png置于文件夹内, 高度为7像素, 宽度随意")
    print("读取到以下图像, 请确认:")
    image=img.ImageProcessor("img.png")
    image.print_image()
    inp= input("Y/N:")
    if inp=="Y" or inp=="y":
        now=input("请输入开始的日期(如1919-08-10):")
        day=date(now,"%Y-%m-%d")
        path=input("请输入要创建git仓库的位置(完整路径):")

        git.create_git_repo(path)

        for i in range(7*len(image.pixel_data[0])):
            for j in range(image.pixel_data[i%7][i//7]*3):
                tmp=str(j)
                if len(tmp)<2:
                    tmp="0"+tmp
                time=f"{now} 12:00:{tmp}"
                write.append_line_to_file(path,"DrawOnGitHub.txt",f"{time}\n")
            
                git.commit_git(time)

            now=day.get_next_day("%Y-%m-%d")
    