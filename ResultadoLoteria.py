from html.parser import HTMLParser

arquivo=open('D_quina.htm','r')
saida=open(r'c:\temp\D_quina.txt','w')

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        #print("Encountered some data  :", data)
        saida.write(data)


for linha in arquivo:
    parser = MyHTMLParser()
    parser.feed(linha)    
    
arquivo.close()
saida.close()
