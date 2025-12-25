#include <iostream>
#include <string>
#include <fstream>
#include <filesystem>
#include <vector>
#include <unordered_map>

using namespace std;
namespace fs = filesystem;

enum TokenType {
    tok_EOF = -1,
    tok_IDENTIFIER,

    tok_SEMICOLON,
    tok_DOT,
    tok_COMMA,
    tok_COLON,

    tok_OPEN_BRACKET,
    tok_CLOSE_BRACKET,
    tok_OPEN_SQUARE,
    tok_CLOSE_SQUARE,
    tok_OPEN_CURLY,
    tok_CLOSE_CURLY,

    tok_NUM,
};

std::unordered_map<char, TokenType> tokenmap = {
    {';', tok_SEMICOLON},
    {'.', tok_DOT},
    {',', tok_COMMA},
    {'(', tok_OPEN_BRACKET},
    {')', tok_CLOSE_BRACKET},
    {'{', tok_OPEN_CURLY},
    {'}', tok_CLOSE_CURLY}
};


struct Token {
    TokenType type;
    string value;
};

void lexer(fs::path filepath) {
    fstream programfile(filepath);

    if (!programfile.is_open()) {
        cerr << "Failed to open file" << endl;
    }

    char ch;

    vector<Token> tokens;

    while (programfile.get(ch)) {
        
        if (isdigit(ch)) {
            string number;

            while (isdigit(ch)) {
                number += ch;
                programfile.get(ch);
            }

            tokens.push_back({tok_NUM, number});
        }

        if (isalpha(ch) || ch == '_') {
            string identifier;

            while (isalpha(ch) || ch == '_') {
                identifier += ch;
                programfile.get(ch);
            }

            tokens.push_back({tok_IDENTIFIER, identifier});
        }

        if (tokenmap.count(ch) == 1) {
            TokenType tokentype = tokenmap[ch];
            string value(1, ch);
            tokens.push_back({tokentype, value});
        }
    }
    
    for (Token token : tokens) {
        cout << token.type << "|" << token.value << "|" << endl;
    }

}

int main(int argc, char* argv[]) {
    
    if (argc < 2) {
        cerr << "Not enought args" << endl;
        return 0;
    }

    fs::path relativefilepath = argv[1];

    fs::path filepath = fs::current_path() / relativefilepath;

    if (filepath.extension() != ".df") {
        cerr << "File is not .df" << endl;
    }

    lexer(filepath);

    cout << "completed" << endl;

    return 0;
}

