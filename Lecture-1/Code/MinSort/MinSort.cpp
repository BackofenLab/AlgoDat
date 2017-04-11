void min_sort(int *lst, size_t len) {
	for (int i = 0; i < len; i++) {
		int min = i;

		for (int j = i + 1; j < len; j++)
			if (lst[j] < lst[min])
				min = j;

		if (min != i) {
			int tmp = lst[i];
			lst[i] = lst[min];
			lst[min] = tmp;
		}
	}
}