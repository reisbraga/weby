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

        #cxv = Gtk.Box(Gtk.Orientation.VERTICAL,
        #              homogeneous=True, spacing=10)
        cxv = Gtk.Box()
        cxv.set_orientation(Gtk.Orientation.VERTICAL)
        cxv.set_homogeneous(True)
        cxv.set_spacing(10)

        #cxh = Gtk.Box(Gtk.Orientation.HORIZONTAL,
        #              homogeneous=True, spacing=10)
        cxh = Gtk.Box()
        cxh.set_orientation(Gtk.Orientation.HORIZONTAL)
        cxh.set_homogeneous(True)
        cxh.set_spacing(10)

        rtl_mensagem = Gtk.Label()
        rtl_mensagem.set_label('---X---')

        mensagens = ['Fé', 'Paz', 'Amizade', 'Coragem', 'Esperança']
        for msg in mensagens:
            bt = Gtk.Button()
            bt.connect("clicked", self.exibir_mensagem, rtl_mensagem)

            bt.set_label(msg)
            cxh.add(bt)



        cxv.add(cxh)
        cxv.add(rtl_mensagem)
        jnl.add(cxv)
        jnl.show_all()


    def exibir_mensagem(self, componente=None, dados=None):
        """ Exibe uma mensaem no rótulo """
        msg = componente.get_label()
        msg = msg.lower()
        msg = 'Muita {}!!!'.format(msg)
        dados.set_label(msg)



    def sair(self, componente=None, dados=None):
        """ Finaliza a aplicacao """
        Gtk.main_quit()
        raise SystemExit("Tchau!!!")


if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()
