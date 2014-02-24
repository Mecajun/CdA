for ui in *.ui; do
	pyside-uic $ui > ../cda_${ui%.*}.py
done

