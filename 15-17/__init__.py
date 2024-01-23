import random

input_matrix = lambda n: [[int(input(f"Введите значение элемента [{i}][{j}]: ")) for j in range(n)] for i in range(n)]

generate_matrix = lambda n: [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]

sum_matrices = lambda matrix1, matrix2, n: [[matrix1[i][j] + matrix2[i][j] for j in range(n)] for i in range(n)]

determinant = lambda matrix: matrix[0][0] if len(matrix) == 1 else matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] if len(matrix) == 2 else sum((-1) ** j * matrix[0][j] * determinant([[matrix[i][k] for k in range(len(matrix)) if k != j] for i in range(1, len(matrix))]) for j in range(len(matrix)))

print_matrix = lambda matrix: [print(row) for row in matrix]

def main():
    while True:
        print("Меню:")
        print("1. Ввод матрицы вручную")
        print("2. Сгенерировать матрицу")
        print("3. Решение")
        print("4. Выход")
        choice = (input("Введите номер выбранного пункта: "))
        if choice == "1":
            n = int(input("Введите размерность матрицы: "))
            matrix1 = input_matrix(n)
            matrix2 = input_matrix(n)
            print("Матрица 1:")
            print_matrix(matrix1)
            print("Матрица 2:")
            print_matrix(matrix2)
        elif choice == "2":
            n = int(input("Введите размерность матрицы: "))
            matrix1 = generate_matrix(n)
            matrix2 = generate_matrix(n)
            print("Матрица 1:")
            print_matrix(matrix1)
            print("Матрица 2:")
            print_matrix(matrix2)
        elif choice == "3":
            try:
                sum_matrix = sum_matrices(matrix1, matrix2, n)
                det_matrix1 = determinant(sum_matrix)
                print("Сумма матриц:")
                print_matrix(sum_matrix)
                print("Определитель суммы матриц:")
                print(det_matrix1)
            except NameError:
                print("Ошибка! Пожалуйста, сначала выберите пункт 1 или 2 для ввода или генерации матрицы.")
        elif choice == "4":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите пункт из меню (1-4).")
            print()

if __name__ == "__main__":
    main()