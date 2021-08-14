class test4{
    static void matrix_mul(int ar[][],int rows, int columns)
    {
          int[][] resultMatix = new int[rows][columns];
           for (int i = 0; i < rows; i++) {
                  for (int j = 0; j < columns; j++) {
                        resultMatix[i][j] = ar[i][j] + ar[i][j];
                  }
           }
    }
    static void mul_matrix(int arr[][], int rows, int columns)
    {
        int[][] productMatrix  = new int[rows][columns];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                for (int k = 0; k < columns; k++) {
                    productMatrix[i][j] = productMatrix[i][j] + arr[i][k] * arr[k][j];
                }
            }
        }
    }
}