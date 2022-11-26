# Wordle-proiect-ASC
## Echipa
<p>-Scaunasu Anne-Marie (Grupa 144)</p>
<p>-Grosu Andreea (Grupa 144)</p>
## Scurta descriere
<p>1)Programul "game.py" este jocul Wordle! care poate fi jucat de un player cu un numar nelimitat de incercari.</p>
<p>2)Programul "wordle.py" ofera posibilitatea de a da algoritmului un cuvant sa il gaseasca in cat mai putine incercari (sau nu), apoi scrie intr-un fisier toate cuvintele si incercarile corespunzatoare pentru a-l gasi. Acest program isi termina rularea in aproximativ 7 de minute,iar la final scrie si media de incercari care este 4,46.</p>
<p>In programul "wordle.py" este la inceput o sectiune '#algoritul intern'. In aceasta se fac calculele necesare:</p>
<p>- frecventa fiecrei litere pe fiecare pozitie</p>
<p>- probabilitatea fiecarui cuvant</p>
<p>- informatia oferita de fiecare cuvant</p>
<p>- entropia fiecarui cuvant</p>
<p>- cele mai bune 2 cuvinte de inceput</p>
<p>In cardul sectiunii '#rezolvare' se fac urmatorii pasi sunt 2 parti ale programului separate printr-un if (daca se da cuvant de la tastaura sau nu) si algoritmul de ghicire a cuvintelor.</p>
<p>Algoritul functioneaza astfel:</p>
<p>- se creeaza 7 vectori pentru:</p>
<p>  1. literele gasite pe pozitiile bune (corect)</p>
<p>  2. litera incercata pe prima pozitie, este in cuvant, dar nu pe pozitia incercata (in_cuv0)</p>
<p>  3. litera incercata pe a doua pozitie, este in cuvant, dar nu pe pozitia incercata (in_cuv1)</p>
<p>  4. litera incercata pe a treia pozitie, este in cuvant, dar nu pe pozitia incercata (in_cuv2)</p>
<p>  5. litera incercata pe a patra pozitie, este in cuvant, dar nu pe pozitia incercata (in_cuv3)</p>
<p>  6. litera incercata pe a cincea pozitie, este in cuvant, dar nu pe pozitia incercata (in_cuv4)</p>
<p>  7. literele care nu se afla in cuvant (not_in_cuv)</p>
<p>- daca este la primul pas ia cuvantul 'CAREI'(cuv1), acesta fiind ales pentru ca ne da cea mai multa informatie (cuvant care sa nu contina litere care sa se repete)</p>
<p>- daca este la al doilea pas ia cuvantul 'SOTUL'(cuv2), acesta fiind ales ca al doilea cuvant care ne da cea mai multa informatie fara sa repete litere din cuvantul anterior</p>
<p>- de la al treilea pas mai departe isi gaseste singur cuvantul din dictionarul de probabilitati a cuvintelor cu ajutorul conditiilor date prin cei 7 vectori</p>
<p>- fiecare solutie incercata este scrisa in fisier</p>
<p><sub>Am incercat sa folosim o singura lista cu 5 liste componente, dar am avut probleme de verificare a acesteia in pasii ce urmeaza si am optat pentru o expunere mai usoara a acestora.</sub></p>
## Referinte
<p>https://www.inspiredpython.com/article/solving-wordle-puzzles-with-basic-python</p>
<p>https://www.youtube.com/watch?v=v68zYyaEmEA</p>
