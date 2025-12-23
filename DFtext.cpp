#include <iostream>
#include <string>
#include <fstream>
#include <filesystem>

using namespace std;
namespace fs = filesystem;

fs::path relativefilepath = "DFfiles/test1.df";

void tokenizer(fstream file) {
    
}

int main() {
    
    fs::path filepath = fs::current_path() / relativefilepath;

    if (filepath.extension() != ".df") {
        cerr << "File is not .df" << endl;
    }

    fstream ProgramFile(filepath);

    

    ProgramFile.close();

    return 0;
}

