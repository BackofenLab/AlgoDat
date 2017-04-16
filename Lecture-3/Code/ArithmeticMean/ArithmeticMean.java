float[] arithMean(float[] x) {
	float[] a = new float[x.length];
	for (int i = 0; i < x.length; i++) {
		float s = 0.0f;
		for(int j = 0; j < i + 1; j++)
			s = s + x[j];

		a[i] = s / (i+1)
	}

	return a;
}