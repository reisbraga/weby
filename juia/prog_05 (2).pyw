#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python e Gtk
# Prof. Douglas Machado Tavares

# Caixa eh igual a coracao de mae, sempre cabe mais um :-D

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacao:
    """ Define a interface da aplicacao """

    def __init__(self):
        """ __init__() -> instancia de Aplicacao """
        jnl = Gtk.Window()
        jnl.connect("delete-event", self.sair)
        jnl.set_title("Python e Gtk")
        jnl.set_border_width(10)

        cxh = Gtk.Box(homogeneous=True, spacing=10)
        # cxh = Gtk.Box()
        # cxh.set_homogeneous(True)
        # cxh.set_spacing(10)

        bt_fe = Gtk.Button(label="Fé")
        bt_fe.connect("clicked", self.imprimir_saudacoes, 1)
        cxh.add(bt_fe)

        bt_paz = Gtk.Button(label="Paz")
        bt_paz.connect("clicked", self.imprimir_saudacoes, 3)
        cxh.add(bt_paz)

        bt_coragem = Gtk.Button(label="Coragem")
        bt_coragem.connect("clicked", self.imprimir_saudacoes, 5)
        cxh.add(bt_coragem)

        jnl.add(cxh)
        jnl.show_all()


    def imprimir_saudacoes(self, componente=None, dados=None):
        """ Imprime uma Saudacao """
        msg = componente.get_label()
        print(":-) {} :-)".format(msg*dados))


    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicacao """
        Gtk.main_quit()
        raise SystemExit("Tchau!!!")


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
