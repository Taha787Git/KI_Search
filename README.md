# 🎯 Projekt 1: Tic-Tac-Toe

Dieses Projekt ist Teil des Kurses [CS50’s Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/).

> 💡 **Tipp zur Leseansicht:** Falls du diese Datei gerade als reinen Text mit Markdown-Zeichen siehst, drücke **`STRG` + `SHIFT` + `V`** (Mac: `CMD` + `SHIFT` + `V`) oder klicke oben rechts auf das Vorschau-Symbol, um die formatierte Leseansicht zu aktivieren!

## 🎬 Aufgabenstellung

In diesem Projekt geht es darum, eine Künstliche Intelligenz zu schreiben, die das Spiel Tic-Tac-Toe optimal spielt. Dazu implementierst du den **Minimax-Algorithmus**.
Dein Ziel ist es, ein Programm zu vervollständigen, das für jede gegebene Spielsituation den bestmöglichen Zug berechnet. Da die KI optimal spielt, wird sie niemals verlieren (sie gewinnt oder zwingt ein Unentschieden auf).

### 💻 Deine Aufgabe

Deine Aufgabe ist es, die fehlenden Funktionen in der Datei `tictactoe.py` zu vervollständigen. Das Spielfeld (`board`) wird dabei immer als eine Liste von drei Listen dargestellt, bei der jedes Feld entweder `X`, `O` oder `EMPTY` ist. Das Grundgerüst für die visuelle Darstellung (in `runner.py`) ist bereits fertig.

* **`player(board)`:** Gibt zurück, welcher Spieler (`X` oder `O`) gerade am Zug ist. 
  * Im initialen Spielzustand (leeres Feld) ist immer `X` am Zug. 
  * Wenn das Spiel bereits beendet ist (`terminal(board) == True`), kann die Funktion einen beliebigen Wert zurückgeben.
* **`actions(board)`:** Gibt ein `set` aller möglichen Züge `(i, j)` auf dem aktuellen Spielfeld zurück. 
  * `i` steht für die Reihe (0, 1 oder 2) und `j` für die Spalte (0, 1 oder 2). 
  * Ein Zug ist nur auf Feldern möglich, die aktuell `EMPTY` sind.
* **`result(board, action)`:** Gibt ein *neues* Spielfeld zurück, das entsteht, wenn der Zug `action` ausgeführt wird. 
  * **Wichtig:** Das ursprüngliche Feld darf nicht verändert werden! Nutze z.B. das Modul `copy` für einen *Deep Copy* des Spielfelds. 
  * Wenn der übergebene Zug ungültig ist, sollte eine Exception ausgelöst werden.
* **`winner(board)`:** Gibt den Gewinner des Spiels zurück (`X` oder `O`), falls es einen gibt. 
  * Ein Spieler gewinnt bei drei gleichen Zeichen in einer Reihe, Spalte oder Diagonale. 
  * Gibt es noch keinen Gewinner oder endet das Spiel unentschieden, wird `None` zurückgegeben.
* **`terminal(board)`:** Prüft, ob das Spiel beendet ist. 
  * Gibt `True` zurück, wenn jemand gewonnen hat oder alle Felder belegt sind. Sonst `False`.
* **`utility(board)`:** Gibt den numerischen Wert eines *beendeten* Spielfelds zurück. 
  * `1` wenn `X` gewinnt, `-1` wenn `O` gewinnt, `0` bei einem Unentschieden. 
  * Du darfst davon ausgehen, dass diese Funktion nur aufgerufen wird, wenn `terminal(board)` bereits `True` ist.
* **`minimax(board)`:** Gibt den optimalen Zug als Tupel `(i, j)` für den Spieler zurück, der gerade am Zug ist. 
  * Ist das Spiel bereits beendet, soll `None` zurückgegeben werden.

> 🧠 **Tipp zur Implementierung:** Der Minimax-Algorithmus ist rekursiv. Der Max-Spieler (X) versucht, den Score zu maximieren, während der Min-Spieler (O) versucht, ihn zu minimieren. Um die Berechnungszeit deiner KI deutlich zu verkürzen, kannst du optional **Alpha-Beta-Pruning** (Alpha-Beta-Suche) implementieren, damit der Algorithmus nicht unnötig aussichtslose Züge durchrechnet.

---

### 🐛 Ausführen und manuelles Testen

> ⚠️ **Wichtiger Hinweis zur Ausführung:** Da dieses Spiel ein grafisches Fenster öffnet, kann es **nicht** im Terminal des Devcontainers gestartet werden (Devcontainers unterstützen standardmäßig keine grafische Ausgabe).
> 
> Du musst das Spiel stattdessen im Terminal deines **eigenen lokalen Systems** (also direkt auf deinem Computer) ausführen. Stelle sicher, dass du **Python** lokal installiert hast und installiere Pygame vorab mit dem Befehl: `pip install pygame`.

Damit du prüfen kannst, ob dein Code im echten Einsatz richtig funktioniert, kannst du das Programm manuell in deinem lokalen Terminal starten und selbst gegen deine KI antreten:

Bash

```
python runner.py
```

**Erwarteter Output:**

Es öffnet sich ein grafisches Fenster (gesteuert durch Pygame), in dem du wählen kannst, ob du als X oder O spielen möchtest. Mache deinen Zug per Klick – die KI wird im Hintergrund den Minimax-Algorithmus durchlaufen und optimal antworten!

---

## ✅ Lokales Testen mit `check`

Du kannst automatisch überprüfen, ob dein Code alle Anforderungen der Spezifikation erfüllt. In unserer vorkonfigurierten Container-Umgebung musst du dafür nur den folgenden Alias im Terminal ausführen:

```bash
check
```

Achte auf die Rückmeldungen im Terminal – grüne Smileys bedeuten, dass der jeweilige Test bestanden wurde. 
Wenn dir der `check`-Befehl für alle Tests grüne Smileys anzeigt, hast du die volle Punktzahl für dieses Praktikum erreicht.
