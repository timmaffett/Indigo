#include <future>
#include <string>

#include <gtest/gtest.h>

#include <indigo-inchi.h>

#include "common.h"

using namespace indigo;
using namespace std;
using cstring = const char*;

namespace
{
    string f(const string& smiles)
    {
        const auto indigo = indigoAllocSessionId();
        const auto m = indigoLoadMoleculeFromString(smiles.c_str());

        string result = indigoInchiGetInchi(m);

        indigoFree(m);
        indigoReleaseSessionId(indigo);

        return result;
    }
}

TEST(IndigoInChIThreadsTest, basic)
{
    const auto indigo = indigoAllocSessionId();
    vector<future<string>> futures;
    vector<string> smiles_list;

    int mols = indigoIterateSmilesFile(dataPath("molecules/basic/helma.smi").c_str());

    auto inputCounter = 0;
    while (static_cast<bool>(indigoHasNext(mols)))
    {
        int mol = indigoNext(mols);
        const auto smiles = string(indigoRawData(mol));
        smiles_list.push_back(smiles);
        futures.push_back(std::async(f, smiles));
        indigoFree(mol);
        ++inputCounter;
    }

    auto outputCounter = 0;
    for (auto& future: futures)
    {
        string value = future.get();
        const auto m = indigoLoadMoleculeFromString(smiles_list[outputCounter].c_str());
        const auto inchi = string(indigoInchiGetInchi(m));
        indigoFree(m);
        ASSERT_EQ(value, inchi);
        ++outputCounter;
    }

    ASSERT_EQ(inputCounter, outputCounter);

    indigoFree(mols);
    indigoReleaseSessionId(indigo);
}
