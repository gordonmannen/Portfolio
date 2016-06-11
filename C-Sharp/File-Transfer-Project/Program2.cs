using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Threading.Tasks;

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("File transfer process initiated...\n");

            string startPath = "C:\\Users\\gmannen\\Documents\\Visual Studio 2015\\Projects\\Test A\\";
            string targetPath = "C:\\Users\\gmannen\\Documents\\Visual Studio 2015\\Projects\\Test B\\";
            string fileType = "*.txt";

            Console.WriteLine("From: {0}", startPath);
            Console.WriteLine("To: {0}\n", targetPath);

            string[] txtFilesArray = Directory.GetFiles(startPath, fileType);

            foreach (string file in txtFilesArray)
            {
                if (FileCheck(file))
                {
                    string fileTitle = Path.GetFileName(file);

                    Console.WriteLine("Transfer in progress... {0}", fileTitle);

                    File.Copy(file, targetPath + fileTitle, true);
                }
            }

            Console.WriteLine("\nFile Transfer process complete...");
            Console.ReadLine();
        }

        public static bool FileCheck(string FileName)
        {
            FileInfo fileTitleInfo = new FileInfo(FileName);

            if (fileTitleInfo.LastWriteTime.AddDays(1) >= DateTime.Now)
                return true;
            else
                return false;
        }
    }
