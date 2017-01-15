public class Listelem@\onslide<2->@
{   //2 fields: integer and reference@\onslide<3->@
    //private only available in class
    private int data;@\onslide<3->@
    private Listelem next;
    @\onslide<4->@
    //2 constructors: for instance of class 
    public Listelem(int d)
    { data = d; next = null; }
    @\onslide<5->@
    public Listelem(int d, Listnode n)
    { data = d; next = n; }
    @\onslide<6->@
    //adopted from Mary K.Vernon
    //Introduction to Data Structures

