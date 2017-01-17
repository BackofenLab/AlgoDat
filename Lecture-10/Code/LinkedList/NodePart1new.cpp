class Listelem
{@\onslide<2->@
private:
  int data;
  Listelem* next; @\onslide<3->@//Pointer instead of reference
@\onslide<4->@
public:
  Listelem(int d)
  { data = d; next = NULL; }

  Listelem(int d, Listelem* n)
  { data = d; next = n; }

