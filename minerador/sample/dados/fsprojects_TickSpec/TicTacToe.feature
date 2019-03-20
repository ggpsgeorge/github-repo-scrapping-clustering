﻿Feature: Winning positions

Background:
	Given a board layout:
		| 1 | 2 | 3 |
		| O | O | X |
		| O |   |   |
		| X |   | X |

Scenario: Winning positions
	When a player marks X at <row> <col>	
	Then X wins
	
Examples:
	| row    | col	  | 
	| middle | right  |
	| middle | middle |
	| bottom | middle |