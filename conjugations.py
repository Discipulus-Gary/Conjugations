import random

def conjugate_indicative(i, j, k, l, m):
    if i == 0:
        present_stem = verbs[i][j][1][:-2]
        perfect_stem = verbs[i][j][2][:-1]
        conjugations = [[[[verbs[i][j][0]],     [present_stem + 'mus']],
                         [[present_stem + 's'], [present_stem + 'tis']],
                         [[present_stem + 't'], [present_stem + 'nt']]],
                        [[[present_stem + 'ba' + 'm'], [present_stem + 'ba' + 'mus']],
                         [[present_stem + 'ba' + 's'], [present_stem + 'ba' + 'tis']],
                         [[present_stem + 'ba' + 't'], [present_stem + 'ba' + 'nt']]],
                        [[[present_stem + 'bo'],       [present_stem + 'bi' + 'mus']],
                         [[present_stem + 'bi' + 's'], [present_stem + 'bi' + 'tis']],
                         [[present_stem + 'bi' + 't'], [present_stem + 'bu' + 'nt']]],
                        [[[verbs[i][j][2]],        [perfect_stem + 'imus']],
                         [[perfect_stem + 'isti'], [perfect_stem + 'istis']],
                         [[perfect_stem + 'it'],   [perfect_stem + 'erunt']]],
                        [[[perfect_stem + 'eram'], [perfect_stem + 'eramus']],
                         [[perfect_stem + 'eras'], [perfect_stem + 'eratis']],
                         [[perfect_stem + 'erat'], [perfect_stem + 'erant']]],
                        [[[perfect_stem + 'ero'],  [perfect_stem + 'erimus']],
                         [[perfect_stem + 'eris'], [perfect_stem + 'eritis']],
                         [[perfect_stem + 'erit'], [perfect_stem + 'erint']]],
                        [[[verbs[i][j][0] + 'r'], [present_stem + 'mur']],
                         [[present_stem + 'ris'], [present_stem + 'mini']],
                         [[present_stem + 'tur'], [present_stem + 'ntur']]],
                        [[[present_stem + 'ba' + 'r'],   [present_stem + 'ba' + 'mur']],
                         [[present_stem + 'ba' + 'ris'], [present_stem + 'ba' + 'mini']],
                         [[present_stem + 'ba' + 'tur'], [present_stem + 'ba' + 'ntur']]],
                        [[[present_stem + 'bo' + 'r'],   [present_stem + 'bi' + 'mur']],
                         [[present_stem + 'be' + 'ris'], [present_stem + 'bi' + 'mini']],
                         [[present_stem + 'bi' + 'tur'], [present_stem + 'bu' + 'ntur']]],
                        [[[verbs[i][j][3] + ' sum'], [verbs[i][j][3][:-2] + 'i' + ' sumus']],
                         [[verbs[i][j][3] + ' es'],  [verbs[i][j][3][:-2] + 'i' + ' estis']],
                         [[verbs[i][j][3] + ' est'], [verbs[i][j][3][:-2] + 'i' + ' sunt']]],
                        [[[verbs[i][j][3] + ' eram'], [verbs[i][j][3][:-2] + 'i' + ' eramus']],
                         [[verbs[i][j][3] + ' eras'], [verbs[i][j][3][:-2] + 'i' + ' eratis']],
                         [[verbs[i][j][3] + ' erat'], [verbs[i][j][3][:-2] + 'i' + ' erant']]],
                        [[[verbs[i][j][3] + ' ero'],  [verbs[i][j][3][:-2] + 'i' + ' erimus']],
                         [[verbs[i][j][3] + ' eris'], [verbs[i][j][3][:-2] + 'i' + ' eritis']],
                         [[verbs[i][j][3] + ' erit'], [verbs[i][j][3][:-2] + 'i' + ' erunt']]]]
        return conjugations[k][l][m]
    if i == 1:
        present_stem = verbs[i][j][1][:-2]
        perfect_stem = verbs[i][j][2][:-1]
        conjugations = [[[[verbs[i][j][0]],     [present_stem + 'mus']],
                         [[present_stem + 's'], [present_stem + 'tis']],
                         [[present_stem + 't'], [present_stem + 'nt']]],
                        [[[present_stem + 'ba' + 'm'], [present_stem + 'ba' + 'mus']],
                         [[present_stem + 'ba' + 's'], [present_stem + 'ba' + 'tis']],
                         [[present_stem + 'ba' + 't'], [present_stem + 'ba' + 'nt']]],
                        [[[present_stem + 'bo'],       [present_stem + 'bi' + 'mus']],
                         [[present_stem + 'bi' + 's'], [present_stem + 'bi' + 'tis']],
                         [[present_stem + 'bi' + 't'], [present_stem + 'bu' + 'nt']]],
                        [[[verbs[i][j][2]],        [perfect_stem + 'imus']],
                         [[perfect_stem + 'isti'], [perfect_stem + 'istis']],
                         [[perfect_stem + 'it'],   [perfect_stem + 'erunt']]],
                        [[[perfect_stem + 'eram'], [perfect_stem + 'eramus']],
                         [[perfect_stem + 'eras'], [perfect_stem + 'eratis']],
                         [[perfect_stem + 'erat'], [perfect_stem + 'erant']]],
                        [[[perfect_stem + 'ero'],  [perfect_stem + 'erimus']],
                         [[perfect_stem + 'eris'], [perfect_stem + 'eritis']],
                         [[perfect_stem + 'erit'], [perfect_stem + 'erint']]],
                        [[[verbs[i][j][0] + 'r'], [present_stem + 'mur']],
                         [[present_stem + 'ris'], [present_stem + 'mini']],
                         [[present_stem + 'tur'], [present_stem + 'ntur']]],
                        [[[present_stem + 'ba' + 'r'],   [present_stem + 'ba' + 'mur']],
                         [[present_stem + 'ba' + 'ris'], [present_stem + 'ba' + 'mini']],
                         [[present_stem + 'ba' + 'tur'], [present_stem + 'ba' + 'ntur']]],
                        [[[present_stem + 'bo' + 'r'],   [present_stem + 'bi' + 'mur']],
                         [[present_stem + 'be' + 'ris'], [present_stem + 'bi' + 'mini']],
                         [[present_stem + 'bi' + 'tur'], [present_stem + 'bu' + 'ntur']]],
                        [[[verbs[i][j][3] + ' sum'], [verbs[i][j][3][:-2] + 'i' + ' sumus']],
                         [[verbs[i][j][3] + ' es'],  [verbs[i][j][3][:-2] + 'i' + ' estis']],
                         [[verbs[i][j][3] + ' est'], [verbs[i][j][3][:-2] + 'i' + ' sunt']]],
                        [[[verbs[i][j][3] + ' eram'], [verbs[i][j][3][:-2] + 'i' + ' eramus']],
                         [[verbs[i][j][3] + ' eras'], [verbs[i][j][3][:-2] + 'i' + ' eratis']],
                         [[verbs[i][j][3] + ' erat'], [verbs[i][j][3][:-2] + 'i' + ' erant']]],
                        [[[verbs[i][j][3] + ' ero'],  [verbs[i][j][3][:-2] + 'i' + ' erimus']],
                         [[verbs[i][j][3] + ' eris'], [verbs[i][j][3][:-2] + 'i' + ' eritis']],
                         [[verbs[i][j][3] + ' erit'], [verbs[i][j][3][:-2] + 'i' + ' erunt']]]]
        return conjugations[k][l][m]
    if i == 2:
        present_stem = verbs[i][j][1][:-2]
        perfect_stem = verbs[i][j][2][:-1]
        conjugations = [[[[verbs[i][j][0]],                [present_stem[:-1] + 'i' + 'mus']],
                         [[present_stem[:-1] + 'i' + 's'], [present_stem[:-1] + 'i' + 'tis']],
                         [[present_stem[:-1] + 'i' + 't'], [present_stem[:-1] + 'u' + 'nt']]],
                        [[[present_stem + 'ba' + 'm'], [present_stem + 'ba' + 'mus']],
                         [[present_stem + 'ba' + 's'], [present_stem + 'ba' + 'tis']],
                         [[present_stem + 'ba' + 't'], [present_stem + 'ba' + 'nt']]],
                        [[[present_stem[:-1] + 'a' + 'm'], [present_stem[:-1] + 'e' + 'mus']],
                         [[present_stem[:-1] + 'e' + 's'], [present_stem[:-1] + 'e' + 'tis']],
                         [[present_stem[:-1] + 'e' + 't'], [present_stem[:-1] + 'e' + 'nt']]],
                        [[[verbs[i][j][2]],        [perfect_stem + 'imus']],
                         [[perfect_stem + 'isti'], [perfect_stem + 'istis']],
                         [[perfect_stem + 'it'],   [perfect_stem + 'erunt']]],
                        [[[perfect_stem + 'eram'], [perfect_stem + 'eramus']],
                         [[perfect_stem + 'eras'], [perfect_stem + 'eratis']],
                         [[perfect_stem + 'erat'], [perfect_stem + 'erant']]],
                        [[[perfect_stem + 'ero'],  [perfect_stem + 'erimus']],
                         [[perfect_stem + 'eris'], [perfect_stem + 'eritis']],
                         [[perfect_stem + 'erit'], [perfect_stem + 'erint']]],
                        [[[verbs[i][j][0] + 'r'],            [present_stem[:-1] + 'i' + 'mur']],
                         [[present_stem[:-1] + 'e' + 'ris'], [present_stem[:-1] + 'i' + 'mini']],
                         [[present_stem[:-1] + 'i' + 'tur'], [present_stem[:-1] + 'u' + 'ntur']]],
                        [[[present_stem + 'ba' + 'r'],   [present_stem + 'ba' + 'mur']],
                         [[present_stem + 'ba' + 'ris'], [present_stem + 'ba' + 'mini']],
                         [[present_stem + 'ba' + 'tur'], [present_stem + 'ba' + 'ntur']]],
                        [[[present_stem[:-1] + 'a' + 'r'],   [present_stem[:-1] + 'e' + 'mur']],
                         [[present_stem[:-1] + 'e' + 'ris'], [present_stem[:-1] + 'e' + 'mini']],
                         [[present_stem[:-1] + 'e' + 'tur'], [present_stem[:-1] + 'e' + 'ntur']]],
                        [[[verbs[i][j][3] + ' sum'], [verbs[i][j][3][:-2] + 'i' + ' sumus']],
                         [[verbs[i][j][3] + ' es'],  [verbs[i][j][3][:-2] + 'i' + ' estis']],
                         [[verbs[i][j][3] + ' est'], [verbs[i][j][3][:-2] + 'i' + ' sunt']]],
                        [[[verbs[i][j][3] + ' eram'], [verbs[i][j][3][:-2] + 'i' + ' eramus']],
                         [[verbs[i][j][3] + ' eras'], [verbs[i][j][3][:-2] + 'i' + ' eratis']],
                         [[verbs[i][j][3] + ' erat'], [verbs[i][j][3][:-2] + 'i' + ' erant']]],
                        [[[verbs[i][j][3] + ' ero'],  [verbs[i][j][3][:-2] + 'i' + ' erimus']],
                         [[verbs[i][j][3] + ' eris'], [verbs[i][j][3][:-2] + 'i' + ' eritis']],
                         [[verbs[i][j][3] + ' erit'], [verbs[i][j][3][:-2] + 'i' + ' erunt']]]]
        return conjugations[k][l][m]
    if i == 3:
        present_stem = verbs[i][j][1][:-2]
        perfect_stem = verbs[i][j][2][:-1]
        conjugations = [[[[verbs[i][j][0]],                [present_stem[:-1] + 'i' + 'mus']],
                         [[present_stem[:-1] + 'i' + 's'], [present_stem[:-1] + 'i' + 'tis']],
                         [[present_stem[:-1] + 'i' + 't'], [present_stem[:-1] + 'iu' + 'nt']]],
                        [[[present_stem[:-1] + 'ie' + 'ba' + 'm'], [present_stem[:-1] + 'ie' + 'ba' + 'mus']],
                         [[present_stem[:-1] + 'ie' + 'ba' + 's'], [present_stem[:-1] + 'ie' + 'ba' + 'tis']],
                         [[present_stem[:-1] + 'ie' + 'ba' + 't'], [present_stem[:-1] + 'ie' + 'ba' + 'nt']]],
                        [[[present_stem[:-1] + 'i' + 'a' + 'm'], [present_stem[:-1] + 'i' + 'e' + 'mus']],
                         [[present_stem[:-1] + 'i' + 'e' + 's'], [present_stem[:-1] + 'i' + 'e' + 'tis']],
                         [[present_stem[:-1] + 'i' + 'e' + 't'], [present_stem[:-1] + 'i' + 'e' + 'nt']]],
                        [[[verbs[i][j][2]],        [perfect_stem + 'imus']],
                         [[perfect_stem + 'isti'], [perfect_stem + 'istis']],
                         [[perfect_stem + 'it'],   [perfect_stem + 'erunt']]],
                        [[[perfect_stem + 'eram'], [perfect_stem + 'eramus']],
                         [[perfect_stem + 'eras'], [perfect_stem + 'eratis']],
                         [[perfect_stem + 'erat'], [perfect_stem + 'erant']]],
                        [[[perfect_stem + 'ero'],  [perfect_stem + 'erimus']],
                         [[perfect_stem + 'eris'], [perfect_stem + 'eritis']],
                         [[perfect_stem + 'erit'], [perfect_stem + 'erint']]],
                        [[[verbs[i][j][0] + 'r'],            [present_stem[:-1] + 'i' + 'mur']],
                         [[present_stem[:-1] + 'e' + 'ris'], [present_stem[:-1] + 'i' + 'mini']],
                         [[present_stem[:-1] + 'i' + 'tur'], [present_stem[:-1] + 'iu' + 'ntur']]],
                        [[[present_stem[:-1] + 'ie' + 'ba' + 'r'],   [present_stem[:-1] + 'ie' + 'ba' + 'mur']],
                         [[present_stem[:-1] + 'ie' + 'ba' + 'ris'], [present_stem[:-1] + 'ie' + 'ba' + 'mini']],
                         [[present_stem[:-1] + 'ie' + 'ba' + 'tur'], [present_stem[:-1] + 'ie' + 'ba' + 'ntur']]],
                        [[[present_stem[:-1] + 'i' + 'a' + 'r'],   [present_stem[:-1] + 'i' + 'e' + 'mur']],
                         [[present_stem[:-1] + 'i' + 'e' + 'ris'], [present_stem[:-1] + 'i' + 'e' + 'mini']],
                         [[present_stem[:-1] + 'i' + 'e' + 'tur'], [present_stem[:-1] + 'i' + 'e' + 'ntur']]],
                       [[[verbs[i][j][3] + ' sum'],  [verbs[i][j][3][:-2] + 'i' + ' sumus']],
                         [[verbs[i][j][3] + ' es'],  [verbs[i][j][3][:-2] + 'i' + ' estis']],
                         [[verbs[i][j][3] + ' est'], [verbs[i][j][3][:-2] + 'i' + ' sunt']]],
                        [[[verbs[i][j][3] + ' eram'], [verbs[i][j][3][:-2] + 'i' + ' eramus']],
                         [[verbs[i][j][3] + ' eras'], [verbs[i][j][3][:-2] + 'i' + ' eratis']],
                         [[verbs[i][j][3] + ' erat'], [verbs[i][j][3][:-2] + 'i' + ' erant']]],
                        [[[verbs[i][j][3] + ' ero'],  [verbs[i][j][3][:-2] + 'i' + ' erimus']],
                         [[verbs[i][j][3] + ' eris'], [verbs[i][j][3][:-2] + 'i' + ' eritis']],
                         [[verbs[i][j][3] + ' erit'], [verbs[i][j][3][:-2] + 'i' + ' erunt']]]]
        return conjugations[k][l][m]
    present_stem = verbs[i][j][1][:-2]
    perfect_stem = verbs[i][j][2][:-1]
    conjugations = [[[[verbs[i][j][0]],     [present_stem + 'mus']],
                     [[present_stem + 's'], [present_stem + 'tis']],
                     [[present_stem + 't'], [present_stem[:-1] + 'iu' + 'nt']]],
                    [[[present_stem[:-1] + 'ie' + 'ba' + 'm'], [present_stem + 'ie' + 'ba' + 'mus']],
                     [[present_stem[:-1] + 'ie' + 'ba' + 's'], [present_stem + 'ie' + 'ba' + 'tis']],
                     [[present_stem[:-1] + 'ie' + 'ba' + 't'], [present_stem + 'ie' + 'ba' + 'nt']]],
                    [[[present_stem + 'a' + 'm'], [present_stem + 'e' + 'mus']],
                     [[present_stem + 'e' + 's'], [present_stem + 'e' + 'tis']],
                     [[present_stem + 'e' + 't'], [present_stem + 'e' + 'nt']]],
                    [[[verbs[i][j][2]],        [perfect_stem + 'imus']],
                     [[perfect_stem + 'isti'], [perfect_stem + 'istis']],
                     [[perfect_stem + 'it'],   [perfect_stem + 'erunt']]],
                    [[[perfect_stem + 'eram'], [perfect_stem + 'eramus']],
                     [[perfect_stem + 'eras'], [perfect_stem + 'eratis']],
                     [[perfect_stem + 'erat'], [perfect_stem + 'erant']]],
                    [[[perfect_stem + 'ero'],  [perfect_stem + 'erimus']],
                     [[perfect_stem + 'eris'], [perfect_stem + 'eritis']],
                     [[perfect_stem + 'erit'], [perfect_stem + 'erint']]],
                    [[[verbs[i][j][0] + 'r'], [present_stem + 'mur']],
                     [[present_stem + 'ris'], [present_stem + 'mini']],
                     [[present_stem + 'tur'], [present_stem[:-1] + 'iu' + 'ntur']]],
                    [[[present_stem[:-1] + 'ie' + 'ba' + 'r'],   [present_stem[:-1] + 'ie' + 'ba' + 'mur']],
                     [[present_stem[:-1] + 'ie' + 'ba' + 'ris'], [present_stem[:-1] + 'ie' + 'ba' + 'mini']],
                     [[present_stem[:-1] + 'ie' + 'ba' + 'tur'], [present_stem[:-1] + 'ie' + 'ba' + 'ntur']]],
                    [[[present_stem + 'a' + 'r'],   [present_stem + 'e' + 'mur']],
                     [[present_stem + 'e' + 'ris'], [present_stem + 'e' + 'mini']],
                     [[present_stem + 'e' + 'tur'], [present_stem + 'e' + 'ntur']]],
                    [[[verbs[i][j][3] + ' sum'], [verbs[i][j][3][:-2] + 'i' + ' sumus']],
                     [[verbs[i][j][3] + ' es'],  [verbs[i][j][3][:-2] + 'i' + ' estis']],
                     [[verbs[i][j][3] + ' est'], [verbs[i][j][3][:-2] + 'i' + ' sunt']]],
                    [[[verbs[i][j][3] + ' eram'], [verbs[i][j][3][:-2] + 'i' + ' eramus']],
                     [[verbs[i][j][3] + ' eras'], [verbs[i][j][3][:-2] + 'i' + ' eratis']],
                     [[verbs[i][j][3] + ' erat'], [verbs[i][j][3][:-2] + 'i' + ' erant']]],
                    [[[verbs[i][j][3] + ' ero'],  [verbs[i][j][3][:-2] + 'i' + ' erimus']],
                     [[verbs[i][j][3] + ' eris'], [verbs[i][j][3][:-2] + 'i' + ' eritis']],
                     [[verbs[i][j][3] + ' erit'], [verbs[i][j][3][:-2] + 'i' + ' erunt']]]]
    return conjugations[k][l][m]

def conjugate_subjunctive(i, j, k, l, m):
    if i == 0:
        present_stem = verbs[i][j][1][:-2]
        perfect_stem = verbs[i][j][2][:-1]
        conjugations = [[[[present_stem[:-1] + 'e' + 'm'], [present_stem[:-1] + 'e' + 'mus']],
                         [[present_stem[:-1] + 'e' + 's'], [present_stem[:-1] + 'e' + 'tis']],
                         [[present_stem[:-1] + 'e' + 't'], [present_stem[:-1] + 'e' + 'nt']]],
                        [[[present_stem + 'r' + 'e' + 'm'], [present_stem + 'r' + 'e' + 'mus']],
                         [[present_stem + 'r' + 'e' + 's'], [present_stem + 'r' + 'e' + 'tis']],
                         [[present_stem + 'r' + 'e' + 't'], [present_stem + 'r' + 'e' + 'nt']]],
                        [[[perfect_stem + 'eri' + 'm'], [perfect_stem + 'eri' + 'mus']],
                         [[perfect_stem + 'eri' + 's'], [perfect_stem + 'eri' + 'tis']],
                         [[perfect_stem + 'eri' + 't'], [perfect_stem + 'eri' + 'nt']]],
                        [[[perfect_stem + 'isse' + 'm'], [perfect_stem + 'isse' + 'mus']],
                         [[perfect_stem + 'isse' + 's'], [perfect_stem + 'isse' + 'tis']],
                         [[perfect_stem + 'isse' + 't'], [perfect_stem + 'isse' + 'nt']]],
                        [[[present_stem[:-1] + 'e' + 'r'],   [present_stem[:-1] + 'e' + 'mur']],
                         [[present_stem[:-1] + 'e' + 'ris'], [present_stem[:-1] + 'e' + 'mini']],
                         [[present_stem[:-1] + 'e' + 'tur'], [present_stem[:-1] + 'e' + 'ntur']]],
                        [[[present_stem + 'r' + 'e' + 'r'],   [present_stem + 'r' + 'e' + 'mur']],
                         [[present_stem + 'r' + 'e' + 'ris'], [present_stem + 'r' + 'e' + 'mini']],
                         [[present_stem + 'r' + 'e' + 'tur'], [present_stem + 'r' + 'e' + 'ntur']]],
                        [[[verbs[i][j][3] + ' sim'], [verbs[i][j][3][:-2] + 'i' + ' simus']],
                         [[verbs[i][j][3] + ' sis'], [verbs[i][j][3][:-2] + 'i' + ' sitis']],
                         [[verbs[i][j][3] + ' sit'], [verbs[i][j][3][:-2] + 'i' + ' sint']]],
                        [[[verbs[i][j][3] + ' essem'], [verbs[i][j][3][:-2] + 'i' + ' essemus']],
                         [[verbs[i][j][3] + ' esses'], [verbs[i][j][3][:-2] + 'i' + ' essetis']],
                         [[verbs[i][j][3] + ' esset'], [verbs[i][j][3][:-2] + 'i' + ' essent']]]]
        return conjugations[k][l][m]
    if i == 1:
        present_stem = verbs[i][j][1][:-2]
        perfect_stem = verbs[i][j][2][:-1]
        conjugations = [[[[present_stem[:-1] + 'ea' + 'm'], [present_stem[:-1] + 'ea' + 'mus']],
                         [[present_stem[:-1] + 'ea' + 's'], [present_stem[:-1] + 'ea' + 'tis']],
                         [[present_stem[:-1] + 'ea' + 't'], [present_stem[:-1] + 'ea' + 'nt']]],
                        [[[present_stem + 'r' + 'e' + 'm'], [present_stem + 'r' + 'e' + 'mus']],
                         [[present_stem + 'r' + 'e' + 's'], [present_stem + 'r' + 'e' + 'tis']],
                         [[present_stem + 'r' + 'e' + 't'], [present_stem + 'r' + 'e' + 'nt']]],
                        [[[perfect_stem + 'eri' + 'm'], [perfect_stem + 'eri' + 'mus']],
                         [[perfect_stem + 'eri' + 's'], [perfect_stem + 'eri' + 'tis']],
                         [[perfect_stem + 'eri' + 't'], [perfect_stem + 'eri' + 'nt']]],
                        [[[perfect_stem + 'isse' + 'm'], [perfect_stem + 'isse' + 'mus']],
                         [[perfect_stem + 'isse' + 's'], [perfect_stem + 'isse' + 'tis']],
                         [[perfect_stem + 'isse' + 't'], [perfect_stem + 'isse' + 'nt']]],
                        [[[present_stem[:-1] + 'ea' + 'r'],   [present_stem[:-1] + 'ea' + 'mur']],
                         [[present_stem[:-1] + 'ea' + 'ris'], [present_stem[:-1] + 'ea' + 'mini']],
                         [[present_stem[:-1] + 'ea' + 'tur'], [present_stem[:-1] + 'ea' + 'ntur']]],
                        [[[present_stem + 'r' + 'e' + 'r'],   [present_stem + 'r' + 'e' + 'mur']],
                         [[present_stem + 'r' + 'e' + 'ris'], [present_stem + 'r' + 'e' + 'mini']],
                         [[present_stem + 'r' + 'e' + 'tur'], [present_stem + 'r' + 'e' + 'ntur']]],
                        [[[verbs[i][j][3] + ' sim'], [verbs[i][j][3][:-2] + 'i' + ' simus']],
                         [[verbs[i][j][3] + ' sis'], [verbs[i][j][3][:-2] + 'i' + ' sitis']],
                         [[verbs[i][j][3] + ' sit'], [verbs[i][j][3][:-2] + 'i' + ' sint']]],
                        [[[verbs[i][j][3] + ' essem'], [verbs[i][j][3][:-2] + 'i' + ' essemus']],
                         [[verbs[i][j][3] + ' esses'], [verbs[i][j][3][:-2] + 'i' + ' essetis']],
                         [[verbs[i][j][3] + ' esset'], [verbs[i][j][3][:-2] + 'i' + ' essent']]]]
        return conjugations[k][l][m]
    if i == 2:
        present_stem = verbs[i][j][1][:-2]
        perfect_stem = verbs[i][j][2][:-1]
        conjugations = [[[[present_stem[:-1] + 'a' + 'm'], [present_stem[:-1] + 'a' + 'mus']],
                         [[present_stem[:-1] + 'a' + 's'], [present_stem[:-1] + 'a' + 'tis']],
                         [[present_stem[:-1] + 'a' + 't'], [present_stem[:-1] + 'a' + 'nt']]],
                        [[[present_stem + 'r' + 'e' + 'm'], [present_stem + 'r' + 'e' + 'mus']],
                         [[present_stem + 'r' + 'e' + 's'], [present_stem + 'r' + 'e' + 'tis']],
                         [[present_stem + 'r' + 'e' + 't'], [present_stem + 'r' + 'e' + 'nt']]],
                        [[[perfect_stem + 'eri' + 'm'], [perfect_stem + 'eri' + 'mus']],
                         [[perfect_stem + 'eri' + 's'], [perfect_stem + 'eri' + 'tis']],
                         [[perfect_stem + 'eri' + 't'], [perfect_stem + 'eri' + 'nt']]],
                        [[[perfect_stem + 'isse' + 'm'], [perfect_stem + 'isse' + 'mus']],
                         [[perfect_stem + 'isse' + 's'], [perfect_stem + 'isse' + 'tis']],
                         [[perfect_stem + 'isse' + 't'], [perfect_stem + 'isse' + 'nt']]],
                        [[[present_stem[:-1] + 'a' + 'r'],   [present_stem[:-1] + 'a' + 'mur']],
                         [[present_stem[:-1] + 'a' + 'ris'], [present_stem[:-1] + 'a' + 'mini']],
                         [[present_stem[:-1] + 'a' + 'tur'], [present_stem[:-1] + 'a' + 'ntur']]],
                        [[[present_stem + 'r' + 'e' + 'r'],   [present_stem + 'r' + 'e' + 'mur']],
                         [[present_stem + 'r' + 'e' + 'ris'], [present_stem + 'r' + 'e' + 'mini']],
                         [[present_stem + 'r' + 'e' + 'tur'], [present_stem + 'r' + 'e' + 'ntur']]],
                        [[[verbs[i][j][3] + ' sim'], [verbs[i][j][3][:-2] + 'i' + ' simus']],
                         [[verbs[i][j][3] + ' sis'], [verbs[i][j][3][:-2] + 'i' + ' sitis']],
                         [[verbs[i][j][3] + ' sit'], [verbs[i][j][3][:-2] + 'i' + ' sint']]],
                        [[[verbs[i][j][3] + ' essem'], [verbs[i][j][3][:-2] + 'i' + ' essemus']],
                         [[verbs[i][j][3] + ' esses'], [verbs[i][j][3][:-2] + 'i' + ' essetis']],
                         [[verbs[i][j][3] + ' esset'], [verbs[i][j][3][:-2] + 'i' + ' essent']]]]
        return conjugations[k][l][m]
    if i == 3:
        present_stem = verbs[i][j][1][:-2]
        perfect_stem = verbs[i][j][2][:-1]
        conjugations = [[[[present_stem[:-1] + 'ia' + 'm'], [present_stem[:-1] + 'ia' + 'mus']],
                         [[present_stem[:-1] + 'ia' + 's'], [present_stem[:-1] + 'ia' + 'tis']],
                         [[present_stem[:-1] + 'ia' + 't'], [present_stem[:-1] + 'ia' + 'nt']]],
                        [[[present_stem + 'r' + 'e' + 'm'], [present_stem + 'r' + 'e' + 'mus']],
                         [[present_stem + 'r' + 'e' + 's'], [present_stem + 'r' + 'e' + 'tis']],
                         [[present_stem + 'r' + 'e' + 't'], [present_stem + 'r' + 'e' + 'nt']]],
                        [[[perfect_stem + 'eri' + 'm'], [perfect_stem + 'eri' + 'mus']],
                         [[perfect_stem + 'eri' + 's'], [perfect_stem + 'eri' + 'tis']],
                         [[perfect_stem + 'eri' + 't'], [perfect_stem + 'eri' + 'nt']]],
                        [[[perfect_stem + 'isse' + 'm'], [perfect_stem + 'isse' + 'mus']],
                         [[perfect_stem + 'isse' + 's'], [perfect_stem + 'isse' + 'tis']],
                         [[perfect_stem + 'isse' + 't'], [perfect_stem + 'isse' + 'nt']]],
                        [[[present_stem[:-1] + 'ia' + 'r'],   [present_stem[:-1] + 'ia' + 'mur']],
                         [[present_stem[:-1] + 'ia' + 'ris'], [present_stem[:-1] + 'ia' + 'mini']],
                         [[present_stem[:-1] + 'ia' + 'tur'], [present_stem[:-1] + 'ia' + 'ntur']]],
                        [[[present_stem + 'r' + 'e' + 'r'],   [present_stem + 'r' + 'e' + 'mur']],
                         [[present_stem + 'r' + 'e' + 'ris'], [present_stem + 'r' + 'e' + 'mini']],
                         [[present_stem + 'r' + 'e' + 'tur'], [present_stem + 'r' + 'e' + 'ntur']]],
                        [[[verbs[i][j][3] + ' sim'], [verbs[i][j][3][:-2] + 'i' + ' simus']],
                         [[verbs[i][j][3] + ' sis'], [verbs[i][j][3][:-2] + 'i' + ' sitis']],
                         [[verbs[i][j][3] + ' sit'], [verbs[i][j][3][:-2] + 'i' + ' sint']]],
                        [[[verbs[i][j][3] + ' essem'], [verbs[i][j][3][:-2] + 'i' + ' essemus']],
                         [[verbs[i][j][3] + ' esses'], [verbs[i][j][3][:-2] + 'i' + ' essetis']],
                         [[verbs[i][j][3] + ' esset'], [verbs[i][j][3][:-2] + 'i' + ' essent']]]]
        return conjugations[k][l][m]
    present_stem = verbs[i][j][1][:-2]
    perfect_stem = verbs[i][j][2][:-1]
    conjugations = [[[[present_stem[:-1] + 'ia' + 'm'], [present_stem[:-1] + 'ia' + 'mus']],
                     [[present_stem[:-1] + 'ia' + 's'], [present_stem[:-1] + 'ia' + 'tis']],
                     [[present_stem[:-1] + 'ia' + 't'], [present_stem[:-1] + 'ia' + 'nt']]],
                    [[[present_stem + 'r' + 'e' + 'm'], [present_stem + 'r' + 'e' + 'mus']],
                     [[present_stem + 'r' + 'e' + 's'], [present_stem + 'r' + 'e' + 'tis']],
                     [[present_stem + 'r' + 'e' + 't'], [present_stem + 'r' + 'e' + 'nt']]],
                    [[[perfect_stem + 'eri' + 'm'], [perfect_stem + 'eri' + 'mus']],
                     [[perfect_stem + 'eri' + 's'], [perfect_stem + 'eri' + 'tis']],
                     [[perfect_stem + 'eri' + 't'], [perfect_stem + 'eri' + 'nt']]],
                    [[[perfect_stem + 'isse' + 'm'], [perfect_stem + 'isse' + 'mus']],
                     [[perfect_stem + 'isse' + 's'], [perfect_stem + 'isse' + 'tis']],
                     [[perfect_stem + 'isse' + 't'], [perfect_stem + 'isse' + 'nt']]],
                    [[[present_stem[:-1] + 'ia' + 'r'],   [present_stem[:-1] + 'ia' + 'mur']],
                     [[present_stem[:-1] + 'ia' + 'ris'], [present_stem[:-1] + 'ia' + 'mini']],
                     [[present_stem[:-1] + 'ia' + 'tur'], [present_stem[:-1] + 'ia' + 'ntur']]],
                    [[[present_stem + 'r' + 'e' + 'r'],   [present_stem + 'r' + 'e' + 'mur']],
                     [[present_stem + 'r' + 'e' + 'ris'], [present_stem + 'r' + 'e' + 'mini']],
                     [[present_stem + 'r' + 'e' + 'tur'], [present_stem + 'r' + 'e' + 'ntur']]],
                    [[[verbs[i][j][3] + ' sim'], [verbs[i][j][3][:-2] + 'i' + ' simus']],
                     [[verbs[i][j][3] + ' sis'], [verbs[i][j][3][:-2] + 'i' + ' sitis']],
                     [[verbs[i][j][3] + ' sit'], [verbs[i][j][3][:-2] + 'i' + ' sint']]],
                    [[[verbs[i][j][3] + ' essem'], [verbs[i][j][3][:-2] + 'i' + ' essemus']],
                     [[verbs[i][j][3] + ' esses'], [verbs[i][j][3][:-2] + 'i' + ' essetis']],
                     [[verbs[i][j][3] + ' esset'], [verbs[i][j][3][:-2] + 'i' + ' essent']]]]
    return conjugations[k][l][m]

def conjugate_imperative(i, j, k):
    if i == 0:
        present_stem = verbs[i][j][1][:-2]
        conjugations = [[present_stem], [present_stem + 'te']]
        return conjugations[k]
    if i == 1:
        present_stem = verbs[i][j][1][:-2]
        conjugations = [[present_stem], [present_stem + 'te']]
        return conjugations[k]
    if i == 2:
        present_stem = verbs[i][j][1][:-2]
        conjugations = [[present_stem], [present_stem[:-1] + 'i' + 'te']]
        return conjugations[k]
    if i == 3:
        present_stem = verbs[i][j][1][:-2]
        conjugations = [[present_stem], [present_stem[:-1] + 'i' + 'te']]
        return conjugations[k]
    present_stem = verbs[i][j][1][:-2]
    conjugations = [[present_stem], [present_stem + 'te']]
    return conjugations[k]

def conjugate_infinitive(i, j, k):
    if i == 0:
        perfect_stem = verbs[i][j][2][:-1]
        conjugations = [[verbs[i][j][1]],                                             [verbs[i][j][1][:-3] + 'ari'],
                        [perfect_stem + 'isse'],                                      [verbs[i][j][3] + ' esse'],
                        [verbs[i][j][3][:-2] + 'ur' + verbs[i][j][3][-2:] + ' esse'], [verbs[i][j][3][:-2] + 'um' + ' iri']]
        return conjugations[k]
    if i == 1:
        perfect_stem = verbs[i][j][2][:-1]
        conjugations = [[verbs[i][j][1]],                                             [verbs[i][j][1][:-3] + 'eri'],
                        [perfect_stem + 'isse'],                                      [verbs[i][j][3] + ' esse'],
                        [verbs[i][j][3][:-2] + 'ur' + verbs[i][j][3][-2:] + ' esse'], [verbs[i][j][3][:-2] + 'um' + ' iri']]
        return conjugations[k]
    if i == 2:
        perfect_stem = verbs[i][j][2][:-1]
        conjugations = [[verbs[i][j][1]],                                             [verbs[i][j][1][:-3] + 'i'],
                        [perfect_stem + 'isse'],                                      [verbs[i][j][3] + ' esse'],
                        [verbs[i][j][3][:-2] + 'ur' + verbs[i][j][3][-2:] + ' esse'], [verbs[i][j][3][:-2] + 'um' + ' iri']]
        return conjugations[k]
    if i == 3:
        perfect_stem = verbs[i][j][2][:-1]
        conjugations = [[verbs[i][j][1]],                                             [verbs[i][j][1][:-3] + 'i'],
                        [perfect_stem + 'isse'],                                      [verbs[i][j][3] + ' esse'],
                        [verbs[i][j][3][:-2] + 'ur' + verbs[i][j][3][-2:] + ' esse'], [verbs[i][j][3][:-2] + 'um' + ' iri']]
        return conjugations[k]
    perfect_stem = verbs[i][j][2][:-1]
    conjugations = [[verbs[i][j][1]],                                             [verbs[i][j][1][:-3] + 'iri'],
                    [perfect_stem + 'isse'],                                      [verbs[i][j][3] + ' esse'],
                    [verbs[i][j][3][:-2] + 'ur' + verbs[i][j][3][-2:] + ' esse'], [verbs[i][j][3][:-2] + 'um' + ' iri']]
    return conjugations[k]

def conjugate_participle(i, j, k):
    if i == 0:
        present_stem = verbs[i][j][1][:-2]
        conjugations = [[present_stem + 'ns'], 
                                                                            [verbs[i][j][3]],
                        [verbs[i][j][3][:-2] + 'ur' + verbs[i][j][3][-2:]], [present_stem + 'nd' + 'us']]]
        return conjugations[k]
    if i == 1:
        present_stem = verbs[i][j][1][:-2]
        conjugations = [[present_stem + 'ns'],
                                                                            [verbs[i][j][3]],
                        [verbs[i][j][3][:-2] + 'ur' + verbs[i][j][3][-2:]], [present_stem + 'nd' + 'us']]
        return conjugations[k]
    if i == 2:
        present_stem = verbs[i][j][1][:-2]
        conjugations = [[present_stem + 'ns'],
                                                                            [verbs[i][j][3]],
                        [verbs[i][j][3][:-2] + 'ur' + verbs[i][j][3][-2:]], [present_stem + 'nd' + 'us']]
        return conjugations[k]
    if i == 3:
        present_stem = verbs[i][j][1][:-2]
        conjugations = [[present_stem[:-1] + 'ie' + 'ns'],
                                                                            [verbs[i][j][3]],
                        [verbs[i][j][3][:-2] + 'ur' + verbs[i][j][3][-2:]], [present_stem[:-1] + 'ie' + 'nd' + 'us']]
        return conjugations[k]
    present_stem = verbs[i][j][1][:-2]
    conjugations = [[present_stem[:-1] + 'ie' + 'ns'],
                                                                        [verbs[i][j][3]],
                    [verbs[i][j][3][:-2] + 'ur' + verbs[i][j][3][-2:]], [present_stem[:-1] + 'ie' + 'nd' + 'us']]
    return conjugations[k]

def conjugate_gerund(i, j):
    if i == 0:
        present_stem = verbs[i][j][1][:-2]
        return [present_stem + 'nd' + 'i']
    if i == 1:
        present_stem = verbs[i][j][1][:-2]
        return [present_stem + 'nd' + 'i']
    if i == 2:
        present_stem = verbs[i][j][1][:-2]
        return [present_stem + 'nd' + 'i']
    if i == 3:
        present_stem = verbs[i][j][1][:-2]
        return [present_stem[:-1] + 'ie' + 'nd' + 'i']
    present_stem = verbs[i][j][1][:-2]
    return [present_stem[:-1] + 'ie' + 'nd' + 'i']

def conjugate_supine(i, j):
    if i == 0:
        return [verbs[i][j][3][:-2] + 'um']
    if i == 1:
        return [verbs[i][j][3][:-2] + 'um']
    if i == 2:
        return [verbs[i][j][3][:-2] + 'um']
    if i == 3:
        return [verbs[i][j][3][:-2] + 'um']
    return [verbs[i][j][3][:-2] + 'um']
    
files = ['first.txt', 'second.txt', 'third_o.txt', 'third_io.txt', 'fourth.txt']

verbs = []

for i in range(len(files)):
    file = open(files[i], 'r')
    verbs.append([])
    for verb in file:
        verbs[i].append(verb.split())
    file.close()

weights = []

file = open('weights.txt', 'r')
for weight in file:
    weights.append(int(weight))
file.close()

weights.append(1)

choices = [i for i in range(len(weights))]

conjugation = ['first conjugation', 'second conjugation', 'third-o conjugation', 'third-io conjugation', 'fourth conjugation']
tense_voice_indicative = ['present active', 'imperfect active', 'future active', 'perfect active', 'pluperfect active', 'future-perfect active', 'present passive', 'imperfect passive', 'future passive', 'perfect passive (masculine)', 'pluperfect passive (masculine)', 'future-perfect passive (masculine)']
tense_voice_subjunctive = ['present active', 'imperfect active', 'perfect active', 'pluperfect active', 'present passive', 'imperfect passive', 'perfect passive (masculine)', 'pluperfect passive (masculine)']
tense_voice_infinitive = ['present active', 'present passive', 'perfect active', 'perfect passive (masculine nominative singular)', 'future active (masculine nominative singular)', 'future passive']
tense_voice_participle = ['present active (masculine nominative singular)', 'perfect passive (masculine nominative singular)', 'future active (masculine nominative singular)', 'future passive (masculine nominative singular)']
person = ['first person', 'second person', 'third person']
number = ['singular', 'plural']

while True:
    choice = random.choices(choices, weights = weights)[0]

    if choice == len(choices) - 1:
        choice = random.randrange(len(choices) - 1)
    if choice < 360:
        i = choice // 72
        j = random.randrange(len(verbs[i]))
        k = choice % 72 // 6
        l = choice % 72 % 6 // 2
        m = choice % 72 % 6 % 2
        
        conjugations = conjugate_indicative(i, j, k, l, m)
        s = person[l] + ' ' + number[m] + ' ' + tense_voice_indicative[k] + ' indicative'
    elif choice < 600:
        i = (choice - 360) // 48
        j = random.randrange(len(verbs[i]))
        k = (choice - 360) % 48 // 6
        l = (choice - 360) % 48 % 6 // 2
        m = (choice - 360) % 48 % 6 % 2
        
        conjugations = conjugate_subjunctive(i, j, k, l, m)
        s = person[l] + ' ' + number[m] + ' ' + tense_voice_subjunctive[k] + ' subjunctive'
    elif choice < 610:
        i = (choice - 600) // 2
        j = random.randrange(len(verbs[i]))
        k = (choice - 600) % 2

        conjugations = conjugate_imperative(i, j, k)
        s = number[k] + ' imperative'
    elif choice < 640:
        i = (choice - 610) // 6
        j = random.randrange(len(verbs[i]))
        k = (choice - 610) % 6

        conjugations = conjugate_infinitive(i, j, k)
        s = tense_voice_infinitive[k] + ' infinitive'
    elif choice < 660:
        i = (choice - 640) // 4
        j = random.randrange(len(verbs[i]))
        k = (choice - 640) % 4
        
        conjugations = conjugate_participle(i, j, k)
        s = tense_voice_participle[k] + ' participle'
    elif choice < 665:
        i = (choice - 660)
        j = random.randrange(len(verbs[i]))

        conjugations = conjugate_gerund(i, j)
        s = 'gerund (genitive)'
    else:
        i = (choice - 665)
        j = random.randrange(len(verbs[i]))

        conjugations = conjugate_supine(i, j)
        s = 'supine (accusative)'

    _input = input(s + ' of ' + verbs[i][j][0] + ', ' + verbs[i][j][1] + ', ' + verbs[i][j][2] + ', ' + verbs[i][j][3] + ': ')

    while _input == 'R':
        for n in range(len(weights) - 1):
            weights[n] = 1
        file = open('weights.txt', 'w')
        for n in range(len(weights) - 1):
            file.write(str(weights[n]) + '\n')
        file.close()
        _input = input(s + ' of ' + verbs[i][j][0] + ', ' + verbs[i][j][1] + ', ' + verbs[i][j][2] + ', ' + verbs[i][j][3] + ': ')

    if _input in conjugations:
        weights[choice] = min(weights[choice] - 1, 0)
        print('Correct!')
    else:
        weights[choice] += 1
        print('Incorrect!')

    file = open('weights.txt', 'w')
    for n in range(len(weights) - 1):
        file.write(str(weights[n]) + '\n')
    file.close()
        
    print(s + ' of ' + verbs[i][j][0] + ', ' + verbs[i][j][1] + ', ' + verbs[i][j][2] + ', ' + verbs[i][j][3] + ' (' + conjugation[i] + '):')
    
    for _conjugation in conjugations:
        print(_conjugation)

    print()
