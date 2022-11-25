/*
Write a program that takes as an input an integer number n and prints a square and a 
rhombus filled with asterisks (*), with each side long n asterisks. Example: using n=4, the program shows:
   
   *
  ***
 *****
*******
 *****
  ***
   *

*/
import java.util.Scanner;

public class Ex_4.1.3{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    
    
    int row = scan.nextInt();
    int column = row;
    
    for(int i = 0; i<row; i++){
      for(int j = column; j >=i; j--){
      System.out.print(" ");   
      }
      for(int z = 0; z<=i; z++){
        System.out.print("*");
        }
      for(int k = 0; k<i; k++){
        System.out.print("*");
       }
      System.out.println();
    }//end of first outer loop
    
    for(int i = 0; i<row-1; i++){
      for(int j = i; j<column-1; j++){
      System.out.print(" ");
      }
      for(int k = 0; k<row-2; k++){
      System.out.print("*");
      }
      for(int j = 0; j<column-2; j++){
        System.out.print("*");
       }
    System.out.println();  
    }//end of second outer for loop
  
  
  
  }//end of main
}//end of class
