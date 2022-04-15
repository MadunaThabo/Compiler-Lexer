from ast import keyword
from asyncio import constants
import operator


file = open("code.txt", 'a+')

dataType = {
    "num":"number",
    "string":"text string",
    "bool":"boolean"}
binaryOperators = {
    "and":"and operator",
    "or":"or operator",
    "eq":"equal operator",
    "larger":"larger operator",
    "add":"addition operator",
    "sub":"subtraction operator",
    "mult":"multiplication operator"}
unaryOperator = {
    "input":"input operation",
    "not":"not operation",
    ":=":"assign operator"}
constants = {
    "true":"true boolean",
    "false":"false boolean"}
keywords = {
    "main":"main keyword",
    "if":"if keyword",
    "then":"then keyword",
    "else":"else keyword",
    "do":"do keyword",
    "until":"until keyword",
    "while":"while keyword",
    "output":"output keyword",
    "halt":"halt keyword",
    "return":"return keyword",
    "proc":"procedure keyword"}
types = {
    "arr":"array"}
symbols = {
    ";":"semicolon",
    "{":"open curly bracket",
    "}":"close curly bracket",
    "[":"open square bracket",
    "]":"close square bracket",
    "(":"open bracket",
    ")":"close bracket",
    ",":"comma"
    }


