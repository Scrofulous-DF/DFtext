#include <iostream>
#include <filesystem>
#include <fstream>
#include <filesystem>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <format>
#include "../include/json.hpp"


using namespace std;
namespace fs = filesystem;

using json = nlohmann::json;

enum TokenType {
    tok_EOF = -1,
    tok_IDENTIFIER,
    tok_ASSIGNMENT,

    tok_SEMICOLON,
    tok_DOT,
    tok_COMMA,
    tok_COLON,

    tok_OPEN_BRACKET,
    tok_CLOSED_BRACKET,
    tok_OPEN_SQUARE,
    tok_CLOSED_SQUARE,
    tok_OPEN_CURLY,
    tok_CLOSED_CURLY,
    tok_OPEN_ANGLE,
    tok_CLOSED_ANGLE,

    tok_NUM,
    tok_STXT,
    tok_STR,

    tok_BOOL,
};

struct Token {
    TokenType type;
    string value;
};

unordered_map<char, TokenType> singulartokens {
    {'=', tok_ASSIGNMENT},
    {';', tok_SEMICOLON},
    {'.', tok_DOT},
    {',', tok_COMMA},
    {'(', tok_OPEN_BRACKET},
    {')', tok_CLOSED_BRACKET},
    {'[', tok_OPEN_SQUARE},
    {']', tok_CLOSED_SQUARE},
    {'{', tok_OPEN_CURLY},
    {'}', tok_CLOSED_CURLY},
    {'<', tok_OPEN_ANGLE},
    {'>', tok_CLOSED_ANGLE},
};

unordered_map<char, TokenType> wraptokens = {
    {'\'', tok_STR},
    {'"', tok_STXT},
};

vector<Token> lexer(fs::path filepath) {
    fstream programfile(filepath);

    if (!programfile.is_open()) {
        cerr << "Failed to open file" << endl;
    }

    char ch;

    vector<Token> tokens;

    // two types of loops:
    // # 1 loops while ch is a type of character(Identifier and number) and needs a putback so it
    // # 2 loops while ch is not a character

    while (programfile.get(ch)) {
        
        cout << ch;

        if (ch == '#') {

            programfile.get(ch);

            while (ch != '#') {
                programfile.get(ch);
            }
        }

        if (wraptokens.count(ch) == 1) {

            char wrapch = ch;

            programfile.get(ch);

            string value = "";

            while (ch != wrapch) {
                value += ch;
                programfile.get(ch);
            }

            TokenType tokentype = wraptokens[wrapch];

            tokens.push_back({tokentype, value});
        }

        if (isdigit(ch)) {
            string number = "";

            do {
                number += ch;
                programfile.get(ch);
            } while (isdigit(ch));

            programfile.unget();

            tokens.push_back({tok_NUM, number});

            continue;
        }

        if (isalpha(ch) || ch == '_') {
            string identifier = "";

            do {
                identifier += ch;
                programfile.get(ch);
            } while (isalpha(ch) || ch == '_');

            programfile.unget();

            if (identifier == "True" || identifier == "False") {
                tokens.push_back({tok_BOOL, identifier});
            };

            tokens.push_back({tok_IDENTIFIER, identifier});
            
            continue;
        }

        if (singulartokens.count(ch) == 1) {
            TokenType tokentype = singulartokens[ch];
            string value(1, ch);
            tokens.push_back({tokentype, value});
        }
    }

    tokens.push_back({tok_EOF, ""});

    return tokens;
}



void Parser(vector<Token> tokens) {

    for (Token token : tokens) {
        token.type;
    }
}

int main(int argc, char* argv[]) {
    
    for (int i = 0; i < argc; i++) {
        cout << i << endl;
    }

    if (argc < 2) {
        cerr << "Not enought args" << endl;
        return 0;
    }

    cout << argc;

    fs::path relativefilepath = argv[1];

    fs::path filepath = fs::current_path() / relativefilepath;

    if (filepath.extension() != ".df") {
        cerr << "File is not .df" << endl;
    }

    cout << "File passed" << endl;

    vector<Token> tokens = lexer(filepath);

    cout << "Lexer passed" << endl;

    for (Token token : tokens) {
        cout << token.type << "|" << token.value << "|" << endl;
    }

    Parser(tokens);

    cout << "completed" << endl;

    return 0;
}

