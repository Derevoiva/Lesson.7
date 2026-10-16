"""Lesson 7: matrices, fabric estimates and cells."""
from abc import ABC, abstractmethod
from dataclasses import dataclass

class Matrix:
    def __init__(self,rows):
        if not rows or not rows[0] or any(len(row)!=len(rows[0]) for row in rows):
            raise ValueError("Matrix must be non-empty and rectangular")
        self.rows=[list(row) for row in rows]
    def __str__(self):
        return "\n".join("\t".join(map(str,row)) for row in self.rows)
    def __add__(self,other):
        if not isinstance(other,Matrix): return NotImplemented
        if len(self.rows)!=len(other.rows) or len(self.rows[0])!=len(other.rows[0]):
            raise ValueError("Matrix dimensions must match")
        return Matrix([[a+b for a,b in zip(r,s)] for r,s in zip(self.rows,other.rows)])

class Clothing(ABC):
    @property
    @abstractmethod
    def fabric(self): ...
@dataclass
class Coat(Clothing):
    size: float
    @property
    def fabric(self): return self.size/6.5+0.5
@dataclass
class Suit(Clothing):
    height: float
    @property
    def fabric(self): return 2*self.height+0.3
def total_fabric(items): return sum(item.fabric for item in items)

@dataclass(frozen=True)
class Cell:
    quantity: int
    def __post_init__(self):
        if not isinstance(self.quantity,int) or self.quantity<=0:
            raise ValueError("Cell quantity must be a positive integer")
    def __add__(self,other): return Cell(self.quantity+other.quantity) if isinstance(other,Cell) else NotImplemented
    def __sub__(self,other):
        if not isinstance(other,Cell): return NotImplemented
        return Cell(self.quantity-other.quantity)
    def __mul__(self,other): return Cell(self.quantity*other.quantity) if isinstance(other,Cell) else NotImplemented
    def __truediv__(self,other):
        if not isinstance(other,Cell): return NotImplemented
        return Cell(self.quantity//other.quantity)
    def make_order(self,per_row):
        if per_row<=0: raise ValueError("Invalid row width")
        return "\n".join("*"*min(per_row,self.quantity-i)
                         for i in range(0,self.quantity,per_row))
