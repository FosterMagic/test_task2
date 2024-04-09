def total_apartments_price(n_stores: int = 30, m_growth_cost: int = 10, x_start_cost: int = 10000) -> int:
    """
    Формула расчета суммарной стоимости квартир выводится из формулы суммы n членов    арифметической прогрессии: a(n) = (a(1) + a(n)) * n / 2
    В логике расчета учтено, что число этажей в здании может не быть кратно шагу возрастания цены.
    """
    price = 1000
    if n_stores % m_growth_cost == 0:
        growth_count = n_stores // m_growth_cost
        total_sum = ((x_start_cost * m_growth_cost) + (
                x_start_cost * m_growth_cost + (growth_count - 1) * price * m_growth_cost)) * growth_count / 2
        print(total_sum)
    else:
        growth_count = n_stores // m_growth_cost
        total_sum = ((x_start_cost * m_growth_cost) + (
                x_start_cost * m_growth_cost + (growth_count - 1) * price * m_growth_cost)) * growth_count / 2 + (
                            n_stores % m_growth_cost) * (x_start_cost + growth_count * price)

        return total_sum


print(total_apartments_price(25, 10, 10000))