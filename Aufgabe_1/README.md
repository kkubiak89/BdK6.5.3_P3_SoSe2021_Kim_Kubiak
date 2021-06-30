# Aufgabe 1 in BDK6.5.3 (wb/öB) P3 Data Librarianship und Programmierung

## 1. Text-Editor der Wahl
Visual Studio Code. Das Programm habe ich auch schon oft in anderen Kontexten gesehen und kam deswegen auch sehr gut mit der Anwendung zurecht.

## 2. Eine Python-Bibliothek
Seaborn. Mit der Seaborn Library ist es möglich statistische Grafiken in Python einzubringen. Die Basis von Seaborn bilden Matplotlib und pandas. Man kann die Daten, die man in sein Python Skript eigebunden hat, durch Seaborn visualieren. Man kann hier wählen, ob sich für die hier benutzen Daten ein Säulendiagramm ein besten eignet oder vielleicht sogar ein Kerndichteschätze. Das ist sehr praktisch um seine Daten direkt auf diese Art aufbereiten zu können und so etwas nicht "manuell" machen muss.

## 3. Eine Fehlermeldung und ihre Lösung
Um das Publikationsjahr von einer Publikation einzugeben habe ich die Publikations "item1" genannt und wollte dann an die Zeile "pubdate" kommen. Dafür habe ich item1["pubdate:"] eingegeben. Dabei kam folgende Fehlermeldung bei mir raus:
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
~\anaconda3\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
   2894             try:
-> 2895                 return self._engine.get_loc(casted_key)
   2896             except KeyError as err:

pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas\_libs\index.pyx in pandas._libs.index.IndexEngine.get_loc()

pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()

pandas\_libs\hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()

KeyError: 'pubdate:'

The above exception was the direct cause of the following exception:

KeyError                                  Traceback (most recent call last)
<ipython-input-20-963d41b6f39a> in <module>
----> 1 item1["pubdate:"]

~\anaconda3\lib\site-packages\pandas\core\frame.py in __getitem__(self, key)
   2900             if self.columns.nlevels > 1:
   2901                 return self._getitem_multilevel(key)
-> 2902             indexer = self.columns.get_loc(key)
   2903             if is_integer(indexer):
   2904                 indexer = [indexer]

~\anaconda3\lib\site-packages\pandas\core\indexes\base.py in get_loc(self, key, method, tolerance)
   2895                 return self._engine.get_loc(casted_key)
   2896             except KeyError as err:
-> 2897                 raise KeyError(key) from err
   2898 
   2899         if tolerance is not None:

KeyError: 'pubdate:'

## 4. Was ist JupyterLab?
blank

## 5. Was ist der große Unterschied zwischen den Webframeworks flask und Django
blank