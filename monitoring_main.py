#TODO stworzenie funkcji obslugujacej żądane polecenia monitorowania. Głównie Odpalanie monitorowania (z pliku monitoring.py i
#killowanie monitorowania. Najlepiej by było zczytywac dane strony do monitorowania wraz z mailem itd. z JSONa, a podawac jej np. tylko link
#i wartosc co chcemy zrobic. np:
#monitoring_main(link, "kill") by wyszukiwał proces który trzeba zabic i go zabijał.
#czyli bedzie trzeba trzymac jakas strukturke z parami link-idprocesu/jakis odnosnik do niego, zalezy jak dziala ten multiprocessing