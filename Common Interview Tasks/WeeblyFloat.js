//Converting a string to a float without using parseFloat()
// - Morgan J. Howell

function weeblyFloat(float_str){
  var float_equivalent = 0;

  //I'm thinking I should split the string into two parts, left and right parts of the decimal   <-L.R->
  //Doing this will give me a good idea of how to compute the base relative to the position of indices
  var index_of_decimal = float_str.indexOf('.');

  //in the case that a decimal is not included, consider input as "left of decimal" values
  var left_only = false;
  if(index_of_decimal == -1){
    left_only = true;
    index_of_decimal = float_str.length-1;
  }

  //**NOTE: Javascript floats are limited to 64 bits, I'll simplify and equate that to about 18 digits.... Giving all
  //numbers left of the decimal priorty to minimize inaccuracy.
  var digit_count = 0;

  //number may be positive or negative
  var sign_extended = 1;

  //routine for scanning and calculating cumulative value left of decimal
  var left_total = 0.0;
  var current_base = 1.0;
  for(var i=index_of_decimal-1;i>=0;i--){

    //we want to ensure a negative/positive sign is the very first character, otherwise we throw an exception which our
    //switch statement within our manual number converter takes care of
    if((i-1)<0){

      if((float_str.charAt(i)=='-')){
      sign_extended = -1;
      break;
      } 

      if((float_str.charAt(i)=='+')){
      break;
      }
    }

    left_total += convertToNumberManual(float_str.charAt(i)) * current_base;
    current_base *= 10;
    digit_count++;
    if(digit_count==18){ 
      return large_number_above_bounds(float_str);
    }
  }

  //break after this point if we couldn't find a decimal
  if(left_only) return sign_extended*left_total;

  //routine for scanning and calculating cumulative value right of decimal
  var right_total = 0;
  var current_base = 1.0/10.0;
  for(var i=index_of_decimal+1;i<=float_str.length-1;i++){

    right_total += convertToNumberManual(float_str.charAt(i)) * current_base;
    current_base *= 1.0/10.0;
    digit_count++;
    if(digit_count==18) return sign_extended * (left_total+right_total) 

  }

  //add values left of decimal to values right of decimal to arrive at the equivalent float value
  float_equivalent = sign_extended * (left_total + right_total);
  
  return float_equivalent;
};


//In order to avoid using parseInt() or parseFloat() I felt this nasty switch statement would suffice.
function convertToNumberManual(character_num){
  var converted_value;

  switch(character_num){
      case '0':
          converted_value = 0.0;
          break;

      case '1':
          converted_value = 1.0;
          break;

      case '2':
          converted_value = 2.0;
          break;

      case '3':
          converted_value = 3.0;
          break;

      case '4':
          converted_value = 4.0;
          break;

      case '5':
          converted_value = 5.0;
          break;

      case '6':
          converted_value = 6.0;
          break;

      case '7':
          converted_value = 7.0;
          break;

      case '8':
          converted_value = 8.0;
          break;

      case '9':
          converted_value = 9.0;
          break;
      //error is thrown if invalid value is read
      default:
          throw "Invalid character, expected float"
  }

  return converted_value;
};


//to maximize accuracy larger numbers must be read from the most siginificant digit down enforcing the 18 char limit
function large_number_above_bounds(num){
  var left_total = 0.0;
  var most_significant_section = num.substring(0,num.lastIndexOf("."));
  var digits = most_significant_section.length;
  var max_base = (digits > 0) ? digits : most_significant_section.length;
  max_base = Math.pow(10, max_base-1)

  for(var i=0;i<18;i++){

    left_total += num.charAt(i) * max_base;
    max_base /= 10;

  }

  return left_total;
};


// TESTING -0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0// 
//Hope you enjoyed the show! Stick around - more solutions for Weebly to come.

var tester = {
  standard : function(){
  var failed = false;

  var f1 = weeblyFloat("1.0");
  var f2 = weeblyFloat("1198923.021");
  var f3 = weeblyFloat("+2221.0654");
  var f4 = weeblyFloat("-3331.0044020");
  var f5 = weeblyFloat("1999999999999999993333332222111.10");

  failed = !(f1 == 1.0) || !(f2 == 1198923.021) || !(f3 == 2221.0654) || !(f4 == -3331.004402) || !(f5 == 1.9999999999999995e+30 );

  if(failed){
    console.log("check your tests, something went wrong");
    
  } else{
    console.log("you're good to go. Lookin' like Weebly material");
  }

  },

  edge_cases: function(){
  var failed = false;

  try{
    var f1 = weeblyFloat("$%^&*(");
    failed = true;
  } catch(err){
    //pass
  }

  try{
    var f1 = weeblyFloat("234234-23.234234");
    failed = true;
  } catch(err){
    //pass
  }

  try{
    var f1 = weeblyFloat("2342323.234234+");
    failed = true;
  } catch(err){
    //pass
  }

  if(failed){
    console.log("check your tests, something went wrong");
  } else{
    console.log("you're good to go. Lookin' like Weebly material");
  }

  }
};

//run testers by calling tester.standard() and tester.edge_cases()

//tester.standard()
//tester.edge_cases()


