from git import Repo

import os
import copy

import re
import signal
import sys
import time
import pwn
import pdb



def handler_signal(signal, frame):
    print('\n\n [!] Out .............. \n')
    sys.exit(1)

signal.signal(signal.SIGINT, handler_signal)


REPO_DIR = './skale/skale-manager'


# time.sleep(15)

def extract(path):
    #Repo permite especificar la url de un repositorio que luego se guarda en la variable especificada
    repo = Repo(path)
    # print(repo)
    # print(repo.status)

    print('Repository extracted')
    time.sleep(1)
    return repo.iter_commits()

def transform(commits):

    commits = list(commits)
    Reference = len(commits)

    processedCommits = list()
    iterationNumber = 0
    for i in list(commits):
        iterationNumber += 1
        #if 'a' in str(i.message):
        patterns = ['password','key','security','critical']
        for pattern in patterns:
            if ( bool(re.search(pattern, i.message)) ):
                processedCommits.append(i)
        print('Filtering commits:')
        print(str(int((iterationNumber/Reference)*100))+'%','[' + ''.join(['=' for i in range(int((iterationNumber/Reference)*100))])+ str('>') + ''.join([' ' for i in '=' for i in range(int((1 - (iterationNumber/Reference))*100))]) +']')
        time.sleep(0.001)
        os.system('cls')

    return processedCommits

def load(processedCommits):
    Register = open('commitRegister.txt', 'a')
    print('MATCHES FOUND: ')
    for i,commit in enumerate(processedCommits):
        print('matched commit {j:.0f}:\n'.format(j=i) , commit.message)
        Register.write(str(commit.message))
        Register.write('\n\n\n')
    Register.close()

    time.sleep(1)


#para luego poder hacer tests hay que poner un punto de entrada
if __name__ == '__main__':
    repoCommits = extract(REPO_DIR)
    processedCommits = transform(repoCommits)
    load(processedCommits)
    print()




