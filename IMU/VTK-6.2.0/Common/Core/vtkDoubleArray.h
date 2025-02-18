/*=========================================================================

  Program:   Visualization Toolkit
  Module:    vtkDoubleArray.h

  Copyright (c) Ken Martin, Will Schroeder, Bill Lorensen
  All rights reserved.
  See Copyright.txt or http://www.kitware.com/Copyright.htm for details.

     This software is distributed WITHOUT ANY WARRANTY; without even
     the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
     PURPOSE.  See the above copyright notice for more information.

=========================================================================*/
// .NAME vtkDoubleArray - dynamic, self-adjusting array of double
// .SECTION Description
// vtkDoubleArray is an array of values of type double.  It provides
// methods for insertion and retrieval of values and will
// automatically resize itself to hold new data.

#ifndef vtkDoubleArray_h
#define vtkDoubleArray_h

// Tell the template header how to give our superclass a DLL interface.
#if !defined(vtkDoubleArray_cxx)
# define VTK_DATA_ARRAY_TEMPLATE_TYPE double
#endif

#include "vtkCommonCoreModule.h" // For export macro
#include "vtkDataArray.h"
#include "vtkDataArrayTemplate.h" // Real Superclass

// Fake the superclass for the wrappers.
#ifndef __WRAP__
#define vtkDataArray vtkDataArrayTemplate<double>
#endif
class VTKCOMMONCORE_EXPORT vtkDoubleArray : public vtkDataArray
#ifndef __WRAP__
#undef vtkDataArray
#endif
{
public:
  static vtkDoubleArray* New();
  vtkTypeMacro(vtkDoubleArray,vtkDataArray);
  void PrintSelf(ostream& os, vtkIndent indent);

  // This macro expands to the set of method declarations that
  // make up the interface of vtkDataArrayTemplate, which is ignored
  // by the wrappers.
#if defined(__WRAP__) || defined (__WRAP_GCCXML__)
  vtkCreateWrappedArrayInterface(double);
#endif

  // Description:
  // Get the minimum data value in its native type.
  static double GetDataTypeValueMin() { return VTK_DOUBLE_MIN; }

  // Description:
  // Get the maximum data value in its native type.
  static double GetDataTypeValueMax() { return VTK_DOUBLE_MAX; }

protected:
  vtkDoubleArray();
  ~vtkDoubleArray();

private:
  //BTX
  typedef vtkDataArrayTemplate<double> RealSuperclass;
  //ETX
  vtkDoubleArray(const vtkDoubleArray&);  // Not implemented.
  void operator=(const vtkDoubleArray&);  // Not implemented.
};

#endif
