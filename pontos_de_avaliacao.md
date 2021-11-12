# Pontos de Avaliacao

## BU: Analysis of requirements with the end user
- Tem de ser dono da conta
- Idade: 18 < anos < 75
- Residência no país de operação do banco
- Estabilidade laboral: ter contrato de trabalho, trabalhador independente com atividade > a 2 anos, reformado
- Não ter historial de não reembolsos ou reembolsos tardios
- Taxa de esforço menor que 40% (rácio entre o rendimento total do agregado familiar destinada ao pagamento das prestações de créditos até então contraídos)
- Não pode ter residência temporária
- Não pode ter património imóvel hipotecado

## BU: Definition of business goals
- Idade: 25 < anos < 65
- Taxa de esforço menor que 33%
- Não ter historial de não reembolsos ou reembolsos tardios
- Limite no numero de cartoes de credito?


## BU: Translation of business goals into data mining goals
- Idade: (Loan.account_id.birth_number > 25) && (Loan.account_id.birth_number < 65)
- Taxa de esforço (Rendimento / Despesas): TOTAL(Transaction.amount WHERE Transaction.type == '+') / TOTAL(Permanent_Order.account_id.amount) <= 0.33
- Historial de reembolsos: TOTAL(Loan.status) == 'A' 

## DU: Diversity of statistical methods

## DU: complexity of statistical methods

## DU: Interpretation of results of statistical methods