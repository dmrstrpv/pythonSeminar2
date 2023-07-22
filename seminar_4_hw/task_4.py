# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

import datetime

FACTOR = 50
CHARGE_MIN = 30
CHARGE_MAX = 600
CHARGE_WITHDRAWAL = 0.15
ACTION_COUNTER = 3
WITHDRAWAL_DEPOSIT_INTEREST = 0.03
ACC_MAX_BALANCE = 5_000_000
CHARGE_MAX_BALANCE = 0.1


def main():
    menu_dict = {
        1: "withdrawal",
        2: "deposit",
        3: "balance_inquiry",
        4: "exit_menu"
    }
    acc_balance: float = 0
    counter = 0

    while True:

        action = show_menu(menu_dict)

        match action:
            case 1:
                yes, acc_balance = withdrawal(acc_balance)
                if yes:
                    counter += 1
                    acc_log(f'withdrawal success')
                    balance_inquiry(acc_balance)

            case 2:
                yes, acc_balance = deposit(acc_balance)
                if yes:
                    counter += 1
                    acc_log(f'deposit success')
                    balance_inquiry(acc_balance)

            case 3:
                balance_inquiry(acc_balance)
                acc_log(f'balance inquiry')

            case 4:
                exit_menu()
                acc_log(f'exit menu')
                return False

        if counter == ACTION_COUNTER:
            counter = 0
            interest = acc_balance * WITHDRAWAL_DEPOSIT_INTEREST
            acc_balance += interest
            balance_inquiry(acc_balance)


def show_menu(menu_dict: dict[int, str]) -> int:
    for key, value in menu_dict.items():
        print(f'{key} - {value}')
    result = int(input("Select >>> "))
    return result


def withdrawal(acc_balance: float):
    result = False
    balance_inquiry(acc_balance)
    withdrawal_sum = int(input("Enter amount: "))

    if acc_balance > ACC_MAX_BALANCE:
        tax = withdrawal_sum * CHARGE_MAX_BALANCE
        withdrawal_sum -= tax

    if withdrawal_sum % FACTOR == 0:
        commission = withdrawal_sum * CHARGE_WITHDRAWAL
        if commission < CHARGE_MIN:
            commission = CHARGE_MIN
        if commission > CHARGE_MAX:
            commission = CHARGE_MAX
        if acc_balance - withdrawal_sum < 0:
            print("Insufficient funds")
        else:
            acc_balance = acc_balance - withdrawal_sum - commission
            print(f'Amount withdrawn: {withdrawal_sum}, Commission: {commission}')
            result = True
    else:
        print("Unable to complete transaction")

    return result, acc_balance


def deposit(acc_balance: float):
    result = False
    balance_inquiry(acc_balance)
    deposit_sum = int(input("Enter amount: "))

    if acc_balance > ACC_MAX_BALANCE:
        tax = deposit_sum * CHARGE_MAX_BALANCE
        deposit_sum -= tax

    if deposit_sum % FACTOR == 0:
        acc_balance += deposit_sum
        print(f'Amount deposited: {deposit_sum}')
        result = True
    else:
        print("Unable to complete transaction")

    return result, acc_balance


def balance_inquiry(acc_balance: float):
    print(f'Account balance: {acc_balance:.2f}')


def exit_menu():
    print("Thank you")


def acc_log(log: str):
    atm_log = []
    ct = datetime.datetime.now()
    atm_log.append(ct)
    atm_log.append(log)


main()

