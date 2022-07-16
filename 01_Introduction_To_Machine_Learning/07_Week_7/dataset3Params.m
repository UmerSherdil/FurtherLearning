function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

error_ref = 1;

x1 = [1 2 1]; x2 = [0 4 -1];
vals =  [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30];
for i=1:8
  for j=1:8
    test_C = vals(i);
    test_sigma = vals(j);
    model= svmTrain(X, y, test_C, @(x1, x2) gaussianKernel(x1, x2, test_sigma));
    y_predict = svmPredict(model, Xval);
    error_found = mean(double(y_predict ~= yval));
    if error_found < error_ref
      C = test_C;
      sigma = test_sigma;
      error_ref = error_found;
    endif
  endfor  
endfor




% =========================================================================

end
