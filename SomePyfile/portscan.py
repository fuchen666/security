#! coding = utf-8

def main(ip):

    ''' 列阵端口 '''

    try:

        # for x in range(1,256):   # C 段 scan

            # print("192.168.95."+str(x))

            portList = [21,22,23,25,53,67,80,110,139,161,389,443,445,1080,1433,3306,5432,6379,\

                        27017,5000,3389,4848,7001,2601,3389,8080,5900,11211,2181]

            for port in portList:

                data = ("[+]: Checking print info  " + ip + ":" + str(port))

                print(data)

                with open("./Result1.txt", 'a') as r:

                    r.write(str(data) + '\n')

    except Exception as e:

        print("[-]:  info {}")

if __name__ == '__main__':

    inputIP = input("输入")

    main("192.168.234.123")
