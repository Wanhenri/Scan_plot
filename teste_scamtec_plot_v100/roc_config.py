import glob
import matplotlib.pyplot as plt




def open_file(statistic,time,var_1):
        path =r'dadosscantec/' # use your path
        allFiles = glob.glob(path + "/"+str(statistic)+"EXP"+ str(time) + "*.csv")
        print("OK")
        
        return (allFiles)


def figure_plot(title,time,statistic):
        plt.savefig('img/'+ str(title)+str(statistic)+str(time)+'.png')
        return
