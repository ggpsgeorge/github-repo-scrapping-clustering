# language: ru




Функционал: Распределение поступающей оплаты по документам реализации и зачёт аванса контрагента

Как Бухгалтер
Я Хочу: чтобы чтобы при фиксации оплаты от Контрагента происходило распределение поступившей суммы по документам реализации товаров и услуг, по которым существуют задолженности
     И происходила фиксация оплаты в виде аванса, если долг отсутствует

Контекст: 
 Когда есть Конфигурация 'Бухгалтерия 3.0 (Такси)'
 И я запускаю сеанс 1С с ключом TestClient
 И существует Контрагент 'тестовый Контрагент'
 И существует договор 'тестовый договор Контрагента 1' с датой договора 01.01.2014
 И существует услуга 'тестовая услуга 1'
 И существует Документ 'РеализацияТоваровИУслуг1' от 01.01.2014  по контрагенту 'тестовый Контрагент' по договору 'тестовый договор Контрагента 1' по услуге 'тестовая услуга 1' на сумму 1000 руб.
 И существует Документ 'РеализацияТоваровИУслуг2' от 02.01.2014  по контрагенту 'тестовый Контрагент' по договору 'тестовый договор Контрагента 1' по услуге 'тестовая услуга 1' на сумму 300 руб.
 И Введена учетная политика

Сценарий: Поступление суммы достаточной только для погашения существующего долга 
  Допустим 'тестовый Контрагент' хочет оплатить сумму 1100 руб.
  Когда фиксируется оплата по  'тестовый Контрагент' по договору 'тестовый договор Контрагента 1'  на сумму 1100 рублей
  Тогда формируется проводка по счету '62.01' на сумму 1000, где 'субконто3' заполнено как Документ 'РеализацияТоваровИУслуг1' от 01.01.2014
      И формируется проводка по счету '62.01' на сумму 100, где 'субконто3' заполнено как Документ 'РеализацияТоваровИУслуг2' от 02.01.2014
      И на счете '62.01'  остается долг в размере 200 рублей по 'субконто3' Документ 'РеализацияТоваровИУслуг2' от 02.01.2014
	  
	  

Сценарий: Поступление суммы превышающей текущий долг покупателя
  Допустим 'тестовый Контрагент' хочет оплатить сумму 2000 руб.
 Когда фиксируется оплата по  'тестовый Контрагент' по договору 'тестовый договор Контрагента 1'  на сумму 2000 рублей
  Тогда формируется проводка по счету '62.01' на сумму 1000, где 'субконто3' заполнено как Документ 'РеализацияТоваровИУслуг1' от 01.01.2014
       И формируется проводка по счету '62.01' на сумму 300, где 'субконто3' заполнено как Документ 'РеализацияТоваровИУслуг2' от 02.01.2014
       И формируется проводка аванса по счету '62.02' на сумму 700, где 'субконто3' заполнено как сам документ поступления оплаты


