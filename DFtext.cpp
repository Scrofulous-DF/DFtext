#include <iostream>
#include <string>
#include <fstream>
#include <filesystem>

using namespace std;

filesystem::path filecd = "C:/Users/Kyleb/OneDrive/Desktop/Personal_Projects/Github/DFtext/.DFfiles/test1.df";

int main() {
    
    if (filecd.extension() != ".df") {
        cerr << "File is not .df" << endl;
    }

    fstream ProgramFile(filecd);

    char ch;

    while (ProgramFile.get(ch)) {
        cout << ch;
    }

    ProgramFile.close();

    return 0;
}