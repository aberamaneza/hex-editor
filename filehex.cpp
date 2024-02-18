#include <iostream>
#include <fstream>
#include<iomanip>
#include <string>
#include <cstring>

extern "C"{
	std::string data;
	__declspec(dllexport) void hexing(const char* path){
		//std::cout<<path;
		//std::string path = "dll.dll";
		//path = path;
		data = ' ';

		std::ifstream file(path,std::ios::binary);
		if (!file.is_open())
		{
			std::cerr<<"error in open file :("<<std::endl;
			
		}
		std::cout << std::hex << std::setfill('0');
		
		char byte;
		int d;
		while(file.get(byte)){

            std::ostringstream stream;
            stream << std::setw(2) << std::setfill('0') << std::hex << static_cast<int>(static_cast<unsigned char>(byte));
            data += stream.str() + " ";
            d += 1;
            if (d==6){
            	data+="\n";

            	d = 0;
            }

		}
		file.close();
		
	}
	__declspec(dllexport) const char* get_data(){
		

        char* result = new char[data.size() + 1];
        
        strcpy(result, data.c_str());

        return result;
        


	}
	__declspec(dllexport) void free_memory(const char* ptr) {
        delete[] ptr;
    }

}