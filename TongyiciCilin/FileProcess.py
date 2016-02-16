# coding: utf-8
__author__ = 'Chao An'

"""
    预处理哈工大信息检索研究中心同义词词林扩展版.txt文件：
        1.将以'='结尾编码的义项（表示同义词）放到synonym.txt文件中
        2.将以'#'结尾编码的义项（表示相关词）放到related.txt文件中
        3.将以'@'结尾编码的义项（表示独立词）放到independent.txt文件中
"""


def process(file_name, synonym, related, independent):
    synonym_fw = open(synonym, 'w')
    related_fw = open(related, 'w')
    independent_fw = open(independent, 'w')
    with open(file_name, 'r') as fr:
        lines = fr.readlines()
        for line in lines:
            print line.split(' ')[0][-1]
            if line.split(' ')[0][-1] == '=':
                print line[line.find(' '):]
                synonym_fw.write(line[line.find(' ')+1:])
            elif line.split(' ')[0][-1] == '#':
                related_fw.write(line[line.find(' ')+1:])
            elif line.split(' ')[0][-1] == '@':
                independent_fw.write(line[line.find(' ')+1:])
    synonym_fw.close()
    related_fw.close()
    independent_fw.close()

if __name__ == '__main__':
    file_name = './resource/Cilin.txt'
    synonym = './resource/synonym.txt'
    related = './resource/related.txt'
    independent = './resource/independent.txt'
    process(file_name, synonym, related, independent)