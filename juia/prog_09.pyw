#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# Python e Gtk
# Prof: Douglas Machado Tavares

# Tinha um botão no meio do caminho

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Aplicacao:
    '''Define a interface da Aplicação'''

    def __init__(self):
        '''__init__() -> instância de Aplicação'''
        jnl = Gtk.Window()

        jnl.connect('delete-event', self.sair)
        jnl.set_title('Python e Gtk')
        jnl.set_border_width(10)

        bt = Gtk.Button()
        bt.connect('clicked', self.imprimir_saudacoes)
        bt.set_label('Ok pessoal :-)')


        jnl.add(bt)
        bt.show()
        jnl.show()


    def imprimir_saudacoes(self, componente=None, dados=None):
        '''Imprimir uma saudação'''
        print(componente.get_label())


    def sair(self, componente=None, dados=None):
        '''Finaliza a aplicação'''
        Gtk.main_quit()
        print('Tchau!!!')
        raise SystemExit()


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()





