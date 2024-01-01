from tkinterappfile import tkinterApp
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



if __name__ == '__main__':
    tkinterApp()
