# Боєра-Мура,
# Кнута-Морріса-Пратта
# Рабіна-Карпа
import timeit
from search_algo.bm import boyer_moore_search
from search_algo.kmp import kmp_search
from search_algo.rk import rabin_karp_search

with open("articles/article_1.txt", "r", encoding="cp1251") as fp:
    article1 = fp.read()


true_text_a1 = "алгоритмы для новичков. Proglib"
fake_text_a1 = "Palworld"

with open("articles/article_1.txt", "r", encoding="cp1251") as fp:
    article2 = fp.read()

true_text_a2 = "В+-дерево (B+-tree) відрізняється тим"
fake_text_a2 = "Palworld"


def testing_searching(algo, text, pattern):
    def search_text():
        return algo(text, pattern)

    result_time = timeit.timeit(search_text, number=1)
    return result_time


bm_true_a1 = testing_searching(boyer_moore_search, article1, true_text_a1)
bm_fake_a1 = testing_searching(boyer_moore_search, article1, fake_text_a1)

bm_true_a2 = testing_searching(boyer_moore_search, article2, true_text_a2)
bm_fake_a2 = testing_searching(boyer_moore_search, article2, fake_text_a2)

kmp_true_a1 = testing_searching(kmp_search, article1, true_text_a1)
kmp_fake_a1 = testing_searching(kmp_search, article1, fake_text_a1)

kmp_true_a2 = testing_searching(kmp_search, article2, true_text_a2)
kmp_fake_a2 = testing_searching(kmp_search, article2, fake_text_a2)

rk_true_a1 = testing_searching(rabin_karp_search, article1, true_text_a1)
rk_fake_a1 = testing_searching(rabin_karp_search, article1, fake_text_a1)

rk_true_a2 = testing_searching(rabin_karp_search, article2, true_text_a2)
rk_fake_a2 = testing_searching(rabin_karp_search, article2, fake_text_a2)

result_true_search_a1 = [
    (bm_true_a1, "Боєра-Мура"),
    (kmp_true_a1, "Кнута-Морріса-Прата"),
    (rk_true_a1, "Рабіна-Карпа"),
]
result_true_search_a2 = [
    (bm_true_a2, "Боєра-Мура"),
    (kmp_true_a2, "Кнута-Морріса-Прата"),
    (rk_true_a2, "Рабіна-Карпа"),
]

result_markdown = f"""
1. **Результати для алгоритму Боєра-Мура:**
   - Для статті 1:
     - Дійсний підрядок: час виконання - {bm_true_a1} сек
     - Вигаданий підрядок: час виконання - {bm_fake_a1} сек
   - Для статті 2:
     - Дійсний підрядок: час виконання - {bm_true_a1} сек
     - Вигаданий підрядок: час виконання - {bm_fake_a2} сек

2. **Результати для алгоритму Кнута-Морріса-Прата:**
   - Для статті 1:
     - Дійсний підрядок: час виконання - {kmp_true_a1} сек
     - Вигаданий підрядок: час виконання - {kmp_fake_a1} сек
   - Для статті 2:
     - Дійсний підрядок: час виконання - {kmp_true_a2} сек
     - Вигаданий підрядок: час виконання - {kmp_fake_a2} сек


3. **Результати для алгоритму Рабіна-Карпа:**
   - Для статті 1:
     - Дійсний підрядок: час виконання - {rk_true_a1} сек
     - Вигаданий підрядок: час виконання - {rk_fake_a1} сек
   - Для статті 2:
     - Дійсний підрядок: час виконання - {rk_true_a2} сек
     - Вигаданий підрядок: час виконання - {rk_fake_a2} сек

4. **Висновок:**
   - Для статті 1:
     - Найшвидший алгорит {min(result_true_search_a1)[1]} з результатом {min(result_true_search_a1)[0]}  
   - Для статті 2:
     - Найшвидший алгорит {min(result_true_search_a2)[1]} з результатом {min(result_true_search_a2)[0]}  
"""
with open("text_serach_result.md", "w", encoding="utf-8") as fp:
    fp.write(result_markdown)
