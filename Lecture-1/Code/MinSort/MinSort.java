void minSort(int[] lst) {
	for (int i = 0; i < lst.length; i++) {
		int min = i;

		for (int j = i + 1; j < lst.length; j++)
			if (lst[j] < lst[min])
				min = j;

		if (min != i) {
			int tmp = lst[i];
			lst[i] = lst[min];
			lst[min] = tmp;
		}
	}
}