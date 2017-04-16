std::vector<float> arithMean(std::vector<float> x) {
	std::vector<float> a(x.size());
	for (int i = 0; i < x.length; i++) {
		float s = 0.0;
		for(int j = 0; j < i + 1; j++)
			s = s + x[j];

		a.push_back(s / (i+1));
	}

	return a;
}