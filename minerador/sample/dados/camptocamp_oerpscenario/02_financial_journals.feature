###############################################################################
#
#    OERPScenario, OpenERP Functional Tests
#    Copyright 2009 Camptocamp SA
#
##############################################################################
##############################################################################
# Branch      # Module       # Processes     # System
@base_finance   @base_commercial_management

Feature: FINANCIAL JOURNALS CREATION

  @base_finance_journals
  Scenario: FINANCIAL JOURNALS CREATION
   Given I need a "account.journal" with oid: scen.eur_journal
   And having:
     | name                      | value                           |
     | name                      | EUR bank                        |
     | code                      | BEUR                            |
     | type                      | bank                            |
     | default_debit_account_id  | by code: 5121                   |
     | default_credit_account_id | by code: 5121                   |
     | allow_date                | t                               |

   Given I need a "account.journal" with oid: scen.usd_journal
   And having:
     | name                      | value                           |
     | name                      | USD bank                        |
     | code                      | BUSD                            |
     | type                      | bank                            |
     | currency                  | by name: USD                    |
     | default_debit_account_id  | by code: 5122                   |
     | default_credit_account_id | by code: 5122                   |
     | allow_date                | t                               |

   Given I need a "account.journal" with oid: scen.gbp_journal
   And having:
      | name                      | value                           |
      | name                      | GBP bank                        |
      | code                      | BGBP                            |
      | type                      | bank                            |
      | currency                  | by name: GBP                    |
      | default_debit_account_id  | by code: 5123                   |
      | default_credit_account_id | by code: 5123                   |
      | allow_date                | t                               |

   Given I need a "account.journal" with oid: scen.sales_journal
   And having:
      | name                      | value                               |
      | name                      | Sales                               |
      | code                      | SAJ                                 |
      | type                      | sale                                |
      | default_debit_account_id  | by code: 707                        |
      | default_credit_account_id | by code: 707                        |
      | group_invoice_lines       | f                                   |
      | allow_date                | t                                   |

     Given I need a "account.journal" with oid: scen.ref_sales_journal
   And having:
      | name                      | value                               |
      | name                      | Sales credit notes                  |
      | code                      | SCNJ                                |
      | type                      | sale_refund                         |
      | default_debit_account_id  | by code: 707                        |
      | default_credit_account_id | by code: 707                        |
      | group_invoice_lines       | f                                   |
      | allow_date                | t                                   |

    Given I need a "account.journal" with oid: scen.purchases_journal
   And having:
      | name                      | value                               |
      | name                      | Purchases                           |
      | code                      | PUJ                                 |
      | type                      | purchase                            |
      | default_debit_account_id  | by code: 607                        |
      | default_credit_account_id | by code: 607                        |
      | group_invoice_lines       | f                                   |
      | allow_date                | t                                   |

     Given I need a "account.journal" with oid: scen.ref_purchases_journal
   And having:
      | name                      | value                               |
      | name                      | Purchases credit notes              |
      | code                      | PCNJ                                |
      | type                      | purchase_refund                     |
      | default_debit_account_id  | by code: 607                        |
      | default_credit_account_id | by code: 607                        |
      | group_invoice_lines       | f                                   |
      | allow_date                | t                                   |

     Given I need a "account.journal" with oid: scen.misc_journal
   And having:
      | name                      | value                               |
      | name                      | Miscellaneous                       |
      | code                      | MISC                                |
      | type                      | general                             |
      | allow_date                | t                                   |

     Given I need a "account.journal" with oid: scen.misc_journal
   And having:
      | name                      | value                               |
      | name                      | Opening journal                     |
      | code                      | OPEN                                |
      | type                      | situation                           |
      | default_debit_account_id  | by code: 120                        |
      | default_credit_account_id | by code: 120                        |
      | centralisation            | t                                   |


   Given I allow cancelling entries on all journals
