function teste(size: number): void {
  const teste1: any[] = Array(size);
  console.log(teste1, '😁');
}

teste(2);

const range = (start, stop) =>
  Array.from({ length: Math.ceil(stop - start) }, (_, i) => start + i);

console.log(range(0, 5));
